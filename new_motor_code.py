import RPi.GPIO as GPIO
import time

# GPIO.cleanup()

# Define GPIO pins for motor control
pwm_pin = 13  # PWM pin for all motors
in1_pins = [6, 5]  # Input 1 pins for Motors 1, 2, 3, 4
in2_pins = [26, 16]  # Input 2 pins for Motors 1, 2, 3, 4

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([pwm_pin] + in1_pins + in2_pins, GPIO.OUT)

# Set up PWM
pwm = GPIO.PWM(pwm_pin, 100)
pwm.start(0)

def move_forward(speed):
    print("moving through move forward function")

   # Set speed
    pwm.ChangeDutyCycle(speed)

    # Move forward
    for in1, in2 in zip(in1_pins, in2_pins):
        print("changing GPIO output to move forward")
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)



# Move forward at 50% speed for 5 seconds
move_forward(50)
time.sleep(10)

# Stop motors
pwm.ChangeDutyCycle(0)

# Clean up GPIO on exit
GPIO.cleanup()