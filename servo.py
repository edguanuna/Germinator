import RPi.GPIO as GPIO
import time

# Define the GPIO pin for PWM
pwm_pin = 32

# Set the GPIO mode and PWM frequency
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 50)  # 50 Hz frequency

def rotate_motor():
    try:
        while True:
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

            # Wait for a brief moment before repeating the cycle
            time.sleep(1)

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

# Call the function to rotate the motor back and forth
rotate_motor()
