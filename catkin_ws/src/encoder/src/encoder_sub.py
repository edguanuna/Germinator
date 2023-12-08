#!/usr/bin/env python3
# The line above tells Linux that this file is a Python script, and that the OS
# should use the Python interpreter in /usr/bin/env to run it. Don't forget to
# use "chmod +x [filename]" to make this script executable.

# Import the dependencies as described in example_pub.py
import rospy
import RPi.GPIO as GPIO
from encoder.msg import TimeDist
from time import sleep

class trajectorySubscribe:
    def __init__(self):

class MotorControl:
    # Define the callback method which is called whenever this node receives a 
    # message on its subscribed topic. The received message is passed as the first
    # argument to callback().
    def __init__(self):
        rospy.init_node('motorcontrol', anonymous=True)
        self.trajectory = []
        #rospy.Subscriber('/trajectory', Trajectory_Array, self.callback_trajectory)
        self.encoders = TimeDist()
        rospy.Subscriber('/encoder', TimeDist, self.callback)
        # Initialize motor controller
        # suggested to use 100 Hz
        frequency = 100 # initialize to 50 Hz
        GPIO.setmode(GPIO.BCM)

        # Set pins from gpio
        # left
        in1 = 6
        in2 = 5
        enA = 13
        # right
        in3 = 26
        in4 = 16
        # enB = 12

        GPIO.setup([in1, in2, in3, in4, enA], GPIO.OUT)

        pwmA = GPIO.PWM(enA, frequency)
        pwmA.start(0) # initialize duty cycle to 0%
        # Define the GPIO pin for PWM
        pwm_pin = 12

        # Set the GPIO mode and PWM frequency
        GPIO.setup(pwm_pin, GPIO.OUT)
        pwm = GPIO.PWM(pwm_pin, 50)  # 50 Hz frequency

    def rotate_motor(self):
        # Rotate to 180 degrees
        pwm.start(7.5)  # Adjust this value based on your motor and setup
        time.sleep(1.5)
        
        # Smooth transition to 0 degrees
        print("smooth transition to 0 degres")
        for duty_cycle in range(75, 25, -1):  # Decrease duty cycle smoothly
            pwm.ChangeDutyCycle(duty_cycle / 10.0)
            time.sleep(0.05)

        # Stop PWM to stop the motor
        pwm.stop()

        # Wait for a brief moment before reversing the direction
        time.sleep(1)

        # Rotate to 0 degrees
        print("rotating to 0 degrees")
        pwm.start(2.5)  # Adjust this value based on your motor and setup
        time.sleep(2)

        # Smooth transition to 180 degrees
        print("smooth transition to 180 degrees")
        for duty_cycle in range(25, 75):  # Increase duty cycle smoothly
            pwm.ChangeDutyCycle(duty_cycle / 10.0)
            time.sleep(0.05)

        # Stop PWM to stop the motor
        pwm.stop()
    

    def set_speed(self,speed):
    #print("going through set speed function")
    #print("motor", motor)
    # if motor == "A":
    #     pwmA.ChangeDutyCycle(speed)
    # elif motor == "B":
    #     pwmB.ChangeDutyCycle(speed)
    pwmA.ChangeDutyCycle(speed)

    def forward(self,speed, time):
        #print("going through forward function")
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
        set_speed(speed)
        sleep(time)

    def backward(self,speed, time):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
        set_speed(speed)
        sleep(time)

    def stop(self):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        # pwmB.ChangeDutyCycle(0)
        pwmA.ChangeDutyCycle(0)

    def turn_right(self,speed, time):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
        sleep(time)
        stop()

    def turn_left(self,speed, time):
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
        sleep(time)
        stop()

    def callback_trajectory(self, message)
        if not self.trajectory:
            self.trajectory = message
        
    def callback(self, message):
        # Print the contents of the message to the console
        # print("DistanceA: " + message.distanceRight + ", DistanceB: " + message.distanceLeft + ", Sent at: " + str(message.timestamp) + ", Received at: " + str(rospy.get_time()))
        self.encoders = [self.encoders, message]

    def control(self):
        current_yaw = 0
        current_distanceLeft = 0
        current_distanceRight = 0
        for i in range(len(self.trajectory)):
            start_time = rospy.Time.now()
            self.trajectory[i, 0] = goal_x
            self.trajectory[i, 1] = goal_y
            self.trajectory[i, 2] = goal_yaw
            while abs(current_yaw - goal_yaw) > 1:
                if current_yaw > goal_yaw:
                    turn_right(20, 1)
                    sleep(1)
                elif current_yaw < goal_yaw:
                    turn_left(20, 1)
                    sleep(1)
            goal_distance = sqrt(goal_x**2 + goal_y**2)
            while abs(goal_distance - ((current_distanceLeft + current_distanceRight)/2)) > 5:
                forward(20, 1)
                sleep(1)
            while (current_distanceRight - current_distanceLeft) > 10:
                turn_left(20, 1)
                sleep(1)
            while (current_distanceLeft - current_distanceRight) > 10:
                turn_right(20, 1)
                sleep(1)
            if i%100 == 0:
                rotate_motor()
            if self.encoders.time == currenttime
                current_yaw = ((self.encoders.distanceRight - self.encoders.distanceLeft))/6
                current_distanceRight = self.encoders.distanceRight
                current_distanceLeft = self.encoders.distanceLeft



    # Python's syntax for a main() method
if __name__ == '__main__':

        # Run this program as a new node in the ROS computation graph called
        # /listener_<id>, where <id> is a randomly generated numeric string. This
        # randomly generated name means we can start multiple copies of this node
        # without having multiple nodes with the same name, which ROS doesn't allow.
        
    try:
        motor_control = MotorControl()
        motor_control.run()
    except rospy.ROSInterruptException:
        pass
    finally:
        # Cleanup GPIO when the program is exiting
        GPIO.cleanup()
