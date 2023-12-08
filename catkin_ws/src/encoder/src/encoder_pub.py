#!/usr/bin/env python3
import rospy
import RPi.GPIO as GPIO
from encoder.msg import TimeDist

class EncoderNode:
    def __init__(self):
        rospy.init_node('encoder_pub', anonymous=True)

        self.pub = rospy.Publisher('/encoder', TimeDist, queue_size=10)
        self.message = TimeDist()

        self.total_distance_left = 0
        self.total_distance_right = 0
        self.distance_per_pulse = 0

        # Set GPIO mode to BCM
        GPIO.setmode(GPIO.BOARD)

        # Define GPIO pins for left and right encoders
        left_encoder_pin = 13  # Change this to your left encoder pin
        right_encoder_pin = 11  # Change this to your right encoder pin

        # Set up GPIO pins as input with pull-up resistors
        GPIO.setup(left_encoder_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(right_encoder_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Constants
        wheel_diameter_cm = 6
        encoder_resolution = 20  # Change this based on your encoder specifications
        self.distance_per_pulse = (wheel_diameter_cm * 3.14159) / encoder_resolution

        # Add event detection for both rising and falling edges
        GPIO.add_event_detect(left_encoder_pin, GPIO.BOTH, callback=self.left_encoder_callback)
        GPIO.add_event_detect(right_encoder_pin, GPIO.BOTH, callback=self.right_encoder_callback)

        # Create a timer object that will sleep long enough to result in a 10Hz publishing rate
        self.r = rospy.Rate(10)  # 10Hz

    # Callback function for left encoder
    def left_encoder_callback(self, channel):
        self.total_distance_left += self.distance_per_pulse

    # Callback function for right encoder
    def right_encoder_callback(self, channel):
        self.total_distance_right += self.distance_per_pulse

    def encoder_pub(self):
        # Create a new instance of TimeDist
        self.message.distanceRight = self.total_distance_right
        self.message.distanceLeft = self.total_distance_left
        self.message.timestamp = rospy.Time.now()
        print(self.message)
        self.pub.publish(self.message)

    def run(self):
        while not rospy.is_shutdown():
            self.encoder_pub()
            self.r.sleep()

    def cleanup(self):
        # Cleanup GPIO when the program is exiting
        GPIO.cleanup()

if __name__ == '__main__':
    try:
        encoder_node = EncoderNode()
        encoder_node.run()
    except rospy.ROSInterruptException:
        pass
    finally:
        # Cleanup GPIO when the program is exiting
        encoder_node.cleanup()



# #!/usr/bin/env python3
# import rospy
# import RPi.GPIO as GPIO
# import time

# # Import message type
# from encoder.msg import TimeDist
# #from std_msgs.msg import Header

# class encoder:
#     def __init__(self):
#         rospy.init_node('encoder_pub', anonymous=True)

#         # Create an instance of the rospy.Publisher object which we can  use to
#         # publish messages to a topic. This publisher publishes messages of type
#         self.pub = rospy.Publisher('/encoder', TimeDist, queue_size=10) #CHANGE MESSAGE TYPE

#         self.message = TimeDist()
#         # Create a timer object that will sleep long enough to result in a 10Hz
#         # publishing rate
#         self.r = rospy.Rate(10) # 10hz
#         self.total_distance_left = 0
#         self.total_distance_right = 0
#         self.distance_per_pulse = 0
#         while not rospy.is_shutdown():
#             self.encoder_pub()  # Call the callback in the loop
#             self.r.sleep() 

#     # Callback function for left encoder
#     def left_encoder_callback(self, channel):
#         self.total_distance_left += self.distance_per_pulse

#     # Callback function for right encoder
#     def right_encoder_callback(self, channel):
#         self.total_distance_right += self.distance_per_pulse

#     def encoder_pub(self):
#         # Set GPIO mode to BCM
#         GPIO.setmode(GPIO.BOARD)
#         # Loop until the node is killed with Ctrl-C
#     # Define GPIO pins for left and right encoders
#         left_encoder_pin = 13  # Change this to your left encoder pin
#         right_encoder_pin = 11  # Change this to your right encoder pin

#         # Set up GPIO pins as input with pull-up resistors
#         GPIO.setup(left_encoder_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#         GPIO.setup(right_encoder_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#         while not rospy.is_shutdown():

#             ##encoder script

         

#             # Constants
#             wheel_diameter_cm = 6
#             encoder_resolution = 20  # Change this based on your encoder specifications
#             self.distance_per_pulse = (wheel_diameter_cm * 3.14159) / encoder_resolution

#             # Variables to store total distance traveled for left and right wheels

#             # Add event detection for both rising and falling edges
#             GPIO.add_event_detect(left_encoder_pin, GPIO.BOTH, callback=self.left_encoder_callback)
#             GPIO.add_event_detect(right_encoder_pin, GPIO.BOTH, callback=self.right_encoder_callback)

            
#             self.message.distanceRight = self.total_distance_right
#             self.message.distanceLeft = self.total_distance_left
#             self.message.timestamp = rospy.Time.now()
#             #print(self.message)

#             self.pub.publish(self.message)

#             GPIO.cleanup()


# if __name__ == '__main__':

#     # Run this program as a new node in the ROS computation graph called /encoder.
#     rospy.init_node('encoder_pub', anonymous=True)

#     # Check if the node has received a signal to shut down. If not, run the
#     # encoder script.
#     try:
#         encoder()
#     except rospy.ROSInterruptException: pass
