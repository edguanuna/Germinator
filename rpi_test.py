import RPi.GPIO as GPIO
from time import sleep

print("import")

# Set pins from gpio
# left
in1 = 31
in2 = 29
enA = 33
# right
in3 = 37
in4 = 36
enB = 32

# Initialize motor controller
frequency = 15000
GPIO.setmode(GPIO.BOARD)
GPIO.setup([in1, in2, in3, in4, enA, enB], GPIO.OUT)

pwmA = GPIO.PWM(enA, frequency)
pwmB = GPIO.PWM(enB, frequency)
pwmA.start(0)
pwmB.start(0)

def set_speed(motor, speed):
    if motor == "A":
        pwmA.ChangeDutyCycle(speed)
    elif motor == "B":
        pwmB.ChangeDutyCycle(speed)

def forward(motor, speed):
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

# Test each motor
print("left test")
forward("A", 20)
sleep(5)
stop("A")

print("right test")
forward("B", 20)
sleep(5)
stop("B")

# Etc. You can continue to replace the functions in your original script with these new ones.

