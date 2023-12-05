#!/usr/bin/env python

from math import tan
from dcmotor import DCMotor       
from machine import Pin, PWM   
import qwiic_adxl313
from time import sleep
import time
import sys
import scipy.integrate as integrate

print("import")

def MotorControl(goal_x, goal_y, goal_yaw):
  #Set pins from gpio
    #left
  in1 = 27
  in2 = 12
  enA = 13
    #right
  in3 = 15
  in4 = 33
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
  print("Initialized motor controller")

  #Initialize accelerometer
  myAdxl = qwiic_adxl313.QwiicAdxl313()
  if myAdxl.connected == False:
      print("The Qwiic ADXL313 device isn't connected to the system. Please check your connection", \
        file=sys.stderr)
  else:
      print("Device connected successfully.")        

  myAdxl.measureModeOn()
  x = 0
  y = 0
  yaw = 0

  #Integrate accelerometer values continuously to determine x, y, and yaw positions
  x = x + integrate.dblquad(myAdxl.x)
  y = y + integrate.dblquad(myAdxl.y)
  yaw = yaw + tan(y/x)

  #Move to goal yaw
  while abs(goal_yaw - yaw) > 10:   #Fine tune difference parameter
    if goal_yaw < yaw:
      #Turn left
      print("left")
      left_motor.backwards(10)
      right_motor.forward(10)
      sleep(2)
      left_motor.stop()
      right_motor.stop()
      x = x + integrate.dblquad(myAdxl.x)
      y = y + integrate.dblquad(myAdxl.y)
      yaw = yaw + tan(y/x)
    elif goal_yaw > yaw:
       #Turn right
      print("right")
      right_motor.backwards(10)
      left_motor.forward(10)  
      sleep(2)
      left_motor.stop()
      right_motor.stop()
      x = x + integrate.dblquad(myAdxl.x)
      y = y + integrate.dblquad(myAdxl.y)
      yaw = yaw + tan(y/x)


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


if __name__ == '__main__':
	try:
		MotorControl(10, 15, 3)
	except (KeyboardInterrupt, SystemExit) as exErr:
		print("\nEnding Example 1")
		sys.exit(0)
