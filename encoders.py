#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from math import pi

GPIO.setmode(GPIO.BOARD)

encoderIn_A = 11 # input pin for the interrupter 
encoderIn_B = 13
detectState_A = 0 # Variable for reading the encoder status
detectState_B = 0

# Initialize photo-interrupter pin
GPIO.setup(encoderIn_A, GPIO.IN)
GPIO.setup(encoderIn_B, GPIO.IN)
last_state_A = 0
last_state_B = 0
pulse_count_A = 0
pulse_count_B = 0

# Function to read the encoder pulses
def read_encoders():
    global pulse_count_A
    global pulse_count_B
    global last_state_A
    global last_state_B
    detectState_A = GPIO.input(encoderIn_A)
    detectState_B = GPIO.input(encoderIn_B)
    if detectState_A != last_state_A:
        pulse_count_A += 1
    elif detectState_B != last_state_B:
        pulse_count_B += 1
    last_state_A = detectState_A
    last_state_B = detectState_A
    return [pulse_count_A, pulse_count_B]  # Simulated pulse

# Constants
pulse_count_A = 0
pulse_count_B = 0
start_time = time.time()
measurement_interval = 3  # Measurement interval in seconds

try:
    while True:
        # pulses_A = read_encoders()[0]
        pulse_count_A = read_encoders()[0]
        # pulses_B = read_encoders()[1]
        pulse_count_B = read_encoders()[1]

        # Check if the measurement interval has passed
        elapsed_time = time.time() - start_time
        if elapsed_time >= measurement_interval:
            revolutions_A = pulse_count_A / 20
            print("revs", revolutions_A)
            rpm_A = ((pulse_count_A / 20) / elapsed_time) * 60  # Calculate RPM for side A
            print(f"RPM_A: {rpm_A:.2f}")
            distance_A = rpm_A*elapsed_time*pi*6 # Calculate distance in cm
            print(f"Distance_CM_A: {distance_A:.2f}")
            rpm_B = ((pulse_count_B / 20) / elapsed_time) * 60  # Calculate RPM for side A
            print(f"RPM_B: {rpm_B:.2f}")
            distance_B = rpm_B*elapsed_time*pi*6 # Calculate distance in cm
            print(f"Distance_CM_B: {distance_B:.2f}")

            # Reset values for the next interval
            pulse_count_A = 0
            pulse_count_B = 0
            start_time = time.time()
except KeyboardInterrupt:
    print("Measurement stopped by user")

GPIO.cleanup()
