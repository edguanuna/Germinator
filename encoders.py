#!/usr/bin/env python

# import RPi.GPIO as GPIO
# import time
# from math import pi


import RPi.GPIO as GPIO
import time

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
distance_per_pulse = (wheel_diameter_cm * 3.14159) / encoder_resolution

# Variables to store total distance traveled for left and right wheels
total_distance_left = 0
total_distance_right = 0

# Callback function for left encoder
def left_encoder_callback(channel):
    global total_distance_left
    total_distance_left += distance_per_pulse

# Callback function for right encoder
def right_encoder_callback(channel):
    global total_distance_right
    total_distance_right += distance_per_pulse

# Add event detection for both rising and falling edges
GPIO.add_event_detect(left_encoder_pin, GPIO.BOTH, callback=left_encoder_callback)
GPIO.add_event_detect(right_encoder_pin, GPIO.BOTH, callback=right_encoder_callback)

try:
    while True:
        time.sleep(1)  # You can perform other tasks here
        print("left", total_distance_left)
        print("right", total_distance_right)

except KeyboardInterrupt:
    # Cleanup GPIO on Ctrl+C
    GPIO.cleanup()
