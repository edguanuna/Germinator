#!/usr/bin/env python
import rospy

# Import message type
import TimeDist.msg


def encoder_pub():

    # Create an instance of the rospy.Publisher object which we can  use to
    # publish messages to a topic. This publisher publishes messages of type
    pub = rospy.Publisher('encoder', TimeDist, queue_size=10) #CHANGE MESSAGE TYPE
    
    # Create a timer object that will sleep long enough to result in a 10Hz
    # publishing rate
    r = rospy.Rate(10) # 10hz

    # Loop until the node is killed with Ctrl-C
    while not rospy.is_shutdown():
        ##encoder script

        encoder_output = #Array of total distance travelled [timestamp, distanceA, distanceB]
        # Publish our string to the 'chatter_talk' topic
        pub.publish(timestamp, distanceA, distanceB)
        r.sleep()

if __name__ == '__main__':

    # Run this program as a new node in the ROS computation graph called /encoder.
    rospy.init_node('encoder_pub', anonymous=True)

    # Check if the node has received a signal to shut down. If not, run the
    # encoder script.
    try:
        encoder_pub()
    except rospy.ROSInterruptException: pass