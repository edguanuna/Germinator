import RPi.GPIO as GPIO
from time import sleep

print("import")



# Initialize motor controller
frequency = 50 # initialize to 50 Hz
GPIO.setmode(GPIO.BCM)

# Set pins from gpio
# left
in1 = 6
in2 = 5
enA = 13
# right
in3 = 26
in4 = 16
enB = 12

GPIO.setup([in1, in2, in3, in4, enA, enB], GPIO.OUT)

pwmA = GPIO.PWM(enA, frequency)
# pwmB = GPIO.PWM(enB, frequency)
pwmA.start(0) # initialize duty cycle to 0%

# duty_cycle = 50
# pwmA.ChangeDutyCycle(duty_cycle)
# pwmB.start(0)


def set_speed(motor, speed):
    print("going through set speed function")
    if motor == "A":
        pwmA.ChangeDutyCycle(speed)
    elif motor == "B":
        pwmB.ChangeDutyCycle(speed)

def forward(motor, speed):
    print("going through forward function")
    if motor == "A":
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        set_speed("A", speed)
    elif motor == "B":
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
        set_speed("B", speed)

def backward(motor, speed):
    if motor == "A":
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        set_speed("A", speed)
    elif motor == "B":
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
        set_speed("B", speed)

def stop(motor):
    if motor == "A":
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        pwmA.ChangeDutyCycle(0)
    elif motor == "B":
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        pwmB.ChangeDutyCycle(0)

def turn_left(speed, time):
    forward("A", speed)
    backward("B", speed)
    sleep(time)
    stop("A")
    stop("B")

def turn_right(speed, time):
    backward("A", speed)
    forward("B", speed)
    sleep(time)
    stop("A")
    stop("B")

print("forward command going you fuck")
forward("A", 20)



# Test each motor
# print("left test")
# forward("A", 1)
# sleep(5)
# stop("A")

# print("right test")
# forward("B", 1)
# sleep(5)
# stop("B")

# p = GPIO.PWM(enA, 50)
# p.start(50)
# GPIO.cleanup()

# print("Test turn left")
# turn_left(1, 2)
# print("RIGHT")
# turn_right(1, 2)


# Etc. You can continue to replace the functions in your original script with these new ones.
GPIO.cleanup()

