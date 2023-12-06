#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from math import pi

GPIO.setmode(GPIO.BOARD)

encoderIn_A = 11 # input pin for the interrupter 
encoderIn_B = 11
detectState_A = 0 # Variable for reading the encoder status
detectState_B = 0

# Initialize photo-interrupter pin
GPIO.setup(encoderIn_A, GPIO.IN)
GPIO.setup(encoderIn_B, GPIO.IN)

# Function to read the encoder pulses
def read_encoder(side):
    if side == "A":
        detectState_A = GPIO.input(encoderIn_A)
    elif side == "B"
        detectState_B = GPIO.input(encoderIn_B)
    return detectState_A, detectState_B  # Simulated pulse

# Constants
pulse_count_A = 0
pulse_count_B = 0
start_time = time.time()
measurement_interval = 1  # Measurement interval in seconds

try:
    while True:
        pulses_A = read_encoder("A")
        pulse_count_A += pulses_A
        pulses_B = read_encoder("B")
        pulse_count_B += pulses_B

        # Check if the measurement interval has passed
        elapsed_time = time.time() - start_time
        if elapsed_time >= measurement_interval:
            rpm_A = (pulse_count_A / elapsed_time) * 60  # Calculate RPM for side A
            print(f"RPM_A: {rpm_A:.2f}")
            distance_A = rpm_A*elapsed_time*pi*6 # Calculate distance in cm
            print(f"Distance_CM_A: {distance_A:.2f}")
            rpm_B = (pulse_count_B / elapsed_time) * 60  # Calculate RPM for side A
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
