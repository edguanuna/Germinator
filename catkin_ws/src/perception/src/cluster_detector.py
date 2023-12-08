#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from sensor_msgs.msg import CameraInfo # For camera intrinsic parameters
from cv_bridge import CvBridge
import matplotlib.pyplot as plt
import os
import time
import tf
from geometry_msgs.msg import Point, PointStamped
from std_msgs.msg import Header
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from perception.msg import CentroidsArray


PLOTS_DIR = os.path.join(os.getcwd(), 'plots')

class ObjectDetector:
    def __init__(self):
        rospy.init_node('object_detector', anonymous=True)


        self.min_dist_between_centroids = 10.0


        self.bridge = CvBridge()

        self.cv_color_image = None
        self.cv_depth_image = None

        self.color_image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.color_image_callback)
        self.depth_image_sub = rospy.Subscriber("/camera/aligned_depth_to_color/image_raw", Image, self.depth_image_callback)

        self.fx = None
        self.fy = None
        self.cx = None
        self.cy = None

        self.camera_info_sub = rospy.Subscriber("/camera/color/camera_info", CameraInfo, self.camera_info_callback)

        self.tf_listener = tf.TransformListener()  # Create a TransformListener object

        self.centroids = CentroidsArray()
        # self.point_pub = rospy.Publisher("goal_point", Point, queue_size=10)
        # self.image_pub = rospy.Publisher('detected_cup', Image, queue_size=10)
        self.centroids_pub = rospy.Publisher('/object_centroids', CentroidsArray, queue_size=10)

        rospy.spin()

    def camera_info_callback(self, msg):
        # TODO: Extract the intrinsic parameters from the CameraInfo message
        self.fx = msg.K[0]
        self.fy = msg.K[4]
        self.cx = msg.K[2]
        self.cy = msg.K[5]

    def pixel_to_point(self, u, v, depth):
        # TODO: Use the camera intrinsics to convert pixel coordinates to real-world coordinates
        X = ((u - self.cx) *  depth) / self.fx
        Y = ((v - self.cy) *  depth) / self.fy
        Z = depth
        return X, Y, Z

    def color_image_callback(self, msg):
        try:
            # Convert the ROS Image message to an OpenCV image (BGR8 format)
            self.cv_color_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

            # If we have both color and depth images, process them
            if self.cv_depth_image is not None:
                self.process_images()

        except Exception as e:
            print("Error:", e)

    def depth_image_callback(self, msg):
        try:
            # Convert the ROS Image message to an OpenCV image (16UC1 format)
            self.cv_depth_image = self.bridge.imgmsg_to_cv2(msg, "16UC1")

        except Exception as e:
            print("Error:", e)

    def process_images(self):
        # Convert the color image to HSV color space
        hsv = cv2.cvtColor(self.cv_color_image, cv2.COLOR_BGR2HSV)
        # TODO: Define range for cup color in HSV
        # NOTE: You can visualize how this is performing by viewing the result of the segmentation in rviz
        # To see the current HSV values in the center row of the image (where your cup should be), we will print out
        # the HSV mean of the HSV values of the center row. You should add at least +/- 10 to the current values to define your range.
        # mean_hsv_val = np.mean()
        print("Current mean values at center row of image: ", np.mean(hsv[len(hsv)//2], axis=0))
        lower_hsv = (np.array([50, 5, 125]))
        upper_hsv = (np.array([70, 25, 150])) 
        lower_rgb = (240,240,240)
        upper_rgb = (265,265,265)
        # TODO: Threshold the image to get only cup colors
        # HINT: Lookup cv2.inRange() or np.where()
        mask = cv2.inRange(self.cv_color_image, lower_rgb, upper_rgb)

        # TODO: Get the coordinates of the cup points on the mask
        # HINT: Lookup np.where() or np.nonzero()
        y_coords, x_coords = np.where(mask)
        # print(y_coords, x_coords)
        # If there are no detected points, exit
        if len(x_coords) == 0 or len(y_coords) == 0:
            print("No points detected. Is your color filter wrong?")
            return

        # Calculate the center of the detected region by 
        coordinates = np.column_stack((x_coords, y_coords))
        num_objects = 4
        kmeans = KMeans(n_clusters=num_objects,algorithm= "elkan",init='k-means++', random_state=0).fit(coordinates)
        labels = kmeans.labels_

        # PLOTS
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(self.cv_color_image, cv2.COLOR_BGR2RGB))
        plt.title('Original Image')

        for i in range(num_objects):
            object_coords = coordinates[labels == i]
            
            if len(object_coords) == 0:
                print('meow')
                continue
            plt.scatter(object_coords[:, 0], object_coords[:, 1], label=f'Object {i+1}', s=50, alpha = 0.8)


        centroids = []

        for i in range(num_objects):
            object_coords = coordinates[labels == i]
            if len(object_coords) == 0:
                continue

            object_center = np.mean(object_coords, axis=0)
            object_center_x, object_center_y = int(object_center[0]), int(object_center[1])
            # Fetch the depth value at the center
            plt.scatter(object_center_x, object_center_y,  label=f"Centroid {i+1}", color="Black")
            depth = self.cv_depth_image[object_center_y, object_center_x]
            centroids.append([object_center_x,object_center_y, depth])
        print(centroids)

        plt.legend()
        plt.title('Detected Objects')

        # plt.show()

        if self.fx and self.fy and self.cx and self.cy:
            camera_x, camera_y, camera_z = self.pixel_to_point(object_center_x, object_center_y, depth)
            camera_link_x, camera_link_y, camera_link_z = camera_z, -camera_x, -camera_y
            # Convert from mm to m
            camera_link_x /= 1000
            camera_link_y /= 1000
            camera_link_z /= 1000

        # Convert the (X, Y, Z) coordinates from camera frame to odom frame
        try:
            self.tf_listener.waitForTransform("/ar_marker_2", "/camera_link", rospy.Time(), rospy.Duration(10.0))
            point_odom = self.tf_listener.transformPoint("/ar_marker_2", PointStamped(header=Header(stamp=rospy.Time(), frame_id="/camera_link"), point=Point(camera_link_x, camera_link_y, camera_link_z)))
            X_odom, Y_odom, Z_odom = point_odom.point.x, point_odom.point.y, point_odom.point.z
            print("Real-world coordinates in ar_marker_2 frame: (X, Y, Z) = ({:.2f}m, {:.2f}m, {:.2f}m)".format(X_odom, Y_odom, Z_odom))

            centroid_msg = PointStamped(
                header = Header(stamp=rospy.Time.now(), frame_id="/ar_marker_2"),
                point=Point(X_odom, Y_odom, Z_odom)
                )

            # self.centroids_pub.publish(centroid_msg)
            # if X_odom < 0.001 and X_odom > -0.001:
            #     print("Erroneous goal point, not publishing - Is the cup too close to the camera?")
            # else:
            #     print("Pub`-lishing goal point: ", X_odom, Y_odom, Z_odom)
            #     # Publish the transformed point
            #     self.point_pub.publish(Point(X_odom, Y_odom, Z_odom))

            #     # Overlay cup points on color image for visualization
            #     cup_img = self.cv_color_image.copy()
            #     cup_img[y_coords, x_coords] = [0, 0, 255]  # Highlight cup points in red
            #     cv2.circle(cup_img, (center_x, center_y), 5, [0, 255, 0], -1)  # Draw green circle at center
                
            #     # Convert to ROS Image message and publish
            #     ros_image = self.bridge.cv2_to_imgmsg(cup_img, "bgr8")
            #     self.image_pub.publish(ros_image)
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e:
            print("TF Error: " + e)
            return

if __name__ == '__main__':
    ObjectDetector()
