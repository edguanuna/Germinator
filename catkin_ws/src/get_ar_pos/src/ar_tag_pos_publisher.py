#!/usr/bin/env python3
import rospy
import tf2_ros
from ar_track_alvar_msgs.msg import AlvarMarkers
from ar_track_alvar_msgs.msg import AlvarMarker

def callback(data):

    for marker in data.markers:
        rospy.loginfo("Received message of type: %s", type(data.markers[0]))
        pose = marker.pose
        #print(f"Ar Tag ID: {marker.id}")
        #print(f"Position: {pose.pose.position}")
        #print(f"Orientation: {pose.pose.orientation}")
        print(marker)
        print("----")
#I want put all frames in term of the "car" frame but it's not working the oiher file does work for that
def meow(marker):
    tfBuffer = tf2_ros.Buffer() 
    tfListener = tf2_ros.TransformListener(tfBuffer)
    try:
        target_frame = 'ar_marker_2'
        source_frame = 'ar_marker_3'
        trans = tfBuffer.lookup_transform(target_frame, source_frame, rospy.Time())
        transorm_translation = trans.transform.translation
        print(transorm_translation) 
    except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
        rospy.logwarn("Transform lookup failed: %s", str(e))
def listener():
    
        rospy.init_node('ar_tag_listener', anonymous=True)
        rospy.Subscriber('/ar_pose_marker', AlvarMarkers, callback)
        rospy.spin()
    
if __name__ == '__main__':
    listener()
