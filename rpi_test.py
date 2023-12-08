import RPi.GPIO as GPIO
from time import sleep


print("import")

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
# pwmB = GPIO.PWM(enB, frequency)
pwmA.start(0) # initialize duty cycle to 0%

def set_speed(speed):
    #print("going through set speed function")
    #print("motor", motor)
    # if motor == "A":
    #     pwmA.ChangeDutyCycle(speed)
    # elif motor == "B":
    #     pwmB.ChangeDutyCycle(speed)
    pwmA.ChangeDutyCycle(speed)

def forward(speed, time):
    #print("going through forward function")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    set_speed(speed)
    sleep(time)

def backward(speed, time):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    set_speed(speed)
    sleep(time)

def stop():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    # pwmB.ChangeDutyCycle(0)
    pwmA.ChangeDutyCycle(0)

def turn_right(speed, time):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    sleep(time)
    stop()

def turn_left(speed, time):
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    sleep(time)
    stop()

# print("forward command")
# forward("B", 20)
# forward("A", 20)
# sleep(5)
# stop("B")
# stop("A")
# sleep(2)


print("turn left")
# speed, time
# suggested to start testing with speed of 20%
turn_left(20, 2)
sleep(3)
turn_right(20, 2)

GPIO.cleanup()
# turn_left("A", 20)



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

