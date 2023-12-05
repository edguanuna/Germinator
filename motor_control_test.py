from dcmotor import DCMotor       
from machine import Pin, PWM   
from time import sleep

print("import")

#Set pins from gpio
  #left
in1 = 31
in2 = 29
enA = 33
   #right
in3 = 37
in4 = 36
enB = 32

#Initialize motor controller
frequency = 15000       
pin1 = Pin(in1, Pin.OUT)    
pin2 = Pin(in2, Pin.OUT)
enableA = PWM(Pin(enA), frequency)
left_motor = DCMotor(pin1, pin2, enableA, 750, 1023)
pin3 = Pin(in3, Pin.OUT)    
pin4 = Pin(in4, Pin.OUT)
enableB = PWM(Pin(enB), frequency)       
right_motor = DCMotor(pin3, pin4, enableB, 750, 1023)
print("init")

#Left test
print("left test")
left_motor.forward(20)
sleep(5)
left_motor.stop()

#Right test
print("right test")
right_motor.forward(20)
sleep(5)
right_motor.stop()

#Go forward
print("forward")
right_motor.forward(10)    #speed is input
left_motor.forward(10)
sleep(5)
left_motor.stop()
right_motor.stop()

#Go backwards
print("backwards")
left_motor.backwards(10)    #speed is input
right_motor.backwards(10)
sleep(5)
left_motor.stop()
right_motor.stop()

#Turn right
print("right")
right_motor.backwards(10)
left_motor.forward(10)  
sleep(5)
left_motor.stop()
right_motor.stop()

#Turn left
print("left")
left_motor.backwards(10)
right_motor.forward(10)
sleep(5)
left_motor.stop()
right_motor.stop()

#Stop motors
print("stop")
left_motor.stop()
right_motor.stop()
