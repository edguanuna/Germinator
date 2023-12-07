#!/usr/bin/env python3
import tf2_ros
import sys
import rospy





#Gives distances between points


def listener():
    tfBuffer = tf2_ros.Buffer()
    tfListener = tf2_ros.TransformListener(tfBuffer)
    target_frame = 'ar_marker_2'
    source_frame = 'ar_marker_3'
    while not rospy.is_shutdown():
        try:
            trans = tfBuffer.lookup_transform(target_frame, source_frame, rospy.Time())
            #print(trans.transform)
            transorm_translation = trans.transform.translation
            # transfrom_quat = trans.transform.rotation
            print(transorm_translation)
            print("-----")
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            print('aaaaa')
            pass
    # Use our rate object to sleep until it is time to publish again
    r.sleep()



if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called
    # /listener_<id>, where <id> is a randomly generated numeric string. This
    # randomly generated name means we can start multiple copies of this node
    # without having multiple nodes with the same name, which ROS doesn't allow.
    rospy.init_node('listener', anonymous=True)
    listener()
    #listener(sys.argv[2], sys.argv[1])
