#!/usr/bin/env python

import rospy

import tf2_ros
import matplotlib.pyplot as plt
import os
import time
import tf

from geometry_msgs.msg import Point
from std_msgs.msg import Header
from ar_track_alvar_msgs.msg import AlvarMarkers
from get_ar_pos.msg import PointArray

PLOTS_DIR = os.path.join(os.getcwd(), 'plots')

#Puts all points in term of ar_tag_1
class ARDetector:
    def __init__(self):
        rospy.init_node('ar_detector', anonymous=True)

        self.markers = []

        self.tfBuffer = tf2_ros.Buffer() 
        self.tfListener = tf2_ros.TransformListener(self.tfBuffer)
        
        self.points = PointArray()
        self.point_pub = rospy.Publisher("/goal_points", PointArray, queue_size=10)
        
        
        
        self.rate = rospy.Rate(1)
        
        while not rospy.is_shutdown():
            self.get_markers_callback()  # Call the callback in the loop
            self.rate.sleep() 
        

    def get_markers_callback(self):
        # Returns an Array of AR Markers
        try:
            markers_msg = rospy.wait_for_message('/ar_pose_marker', AlvarMarkers, timeout=1.0)
            self.markers = markers_msg.markers
            self.generate_tf()
        except rospy.ROSException as e:
            print("ROS Error: " + str(e))

   
    def generate_tf(self):
        if self.markers:
            car_tag = "ar_marker_1"
            for marker in self.markers:
                ar_tag_id = f"ar_marker_{marker.id}"
                #position = marker.pose.pose.position
                
                try:
                    trans = self.tfBuffer.lookup_transform(car_tag, ar_tag_id, rospy.Time(), rospy.Duration(10.0))
                    transorm_translation = trans.transform.translation
                    X_car, Y_car, Z_car = transorm_translation.x, transorm_translation.y, transorm_translation.z
                    print("Real-world coordinates of ar_marker_{} in Car frame: (X, Y, Z) = ({:.2f}m, {:.2f}m, {:.2f}m)".format(marker.id,X_car, Y_car, Z_car))
                    
                    point_instance = Point()
                    point_instance.x = X_car
                    point_instance.y = Y_car
                    point_instance.z = Z_car
                    
                    self.points.points.append(point_instance)
            
                except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
                    print("TF Error: " + str(e))
                    return
            self.point_pub.publish(self.points)
            self.points = PointArray()
            
if __name__ == '__main__':
    ARDetector()
