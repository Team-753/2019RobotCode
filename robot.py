#!/usr/bin/env python3
import wpilib, ctre, math, logging
from wpilib.drive import MecanumDrive
from networktables import NetworkTables
from wpilib import CameraServer
import numpy
import math
from enum import Enum
import logging
import sys
import time
import threading

cond = threading.Condition()
notified = False


def connectionListener(connected, info):
	print(info, '; Connected=%s' % connected)
	with cond:
		notified = True 
		cond.notify()

# To see messages from networktables, you must setup logging 
NetworkTables.initialize() 
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)
sd = NetworkTables.getTable('SmartDashboard') 

sd.getValue('adjust_x', 0)
sd.getValue('adjust_y', 0)
sd.getValue('adjust_z', 0)

"""with cond:
	print("Waiting")
	if notified != True:
		print("#2")
		cond.wait()
	print("#3"0"""
print("escape")




logging.basicConfig(level=logging.DEBUG)

class MyRobot(wpilib.TimedRobot):
	# Channels on the roboRIO that the motor controllers are plugged in to
	frontLeftChannel = 2
	rearLeftChannel = 7
	frontRightChannel = 3
	rearRightChannel = 1
	# The channel on the driver station that the joystick is connected to
	joystickChannel = 0 
	
	def robotInit(self):
		"""Robot initialization function"""
		self.frontLeftMotor = ctre.WPI_TalonSRX(self.frontLeftChannel)
		self.rearLeftMotor = ctre.WPI_TalonSRX(self.rearLeftChannel)
		self.frontRightMotor = ctre.WPI_TalonSRX(self.frontRightChannel)
		self.rearRightMotor = ctre.WPI_TalonSRX(self.rearRightChannel)
		self.spinnyMotor = ctre.WPI_TalonSRX(0)
		# invert the left side motors
		self.frontRightMotor.setInverted(True)

		# you may need to change or remove this to match your robot
		self.rearRightMotor.setInverted(True)

		self.drive = MecanumDrive(
			self.frontLeftMotor,
			self.rearLeftMotor,
			self.frontRightMotor,
			self.rearRightMotor,
		)

		self.drive.setExpiration(0.1)
		self.frontLeftMotor.setSafetyEnabled(False)
		self.frontRightMotor.setSafetyEnabled(False)
		self.rearLeftMotor.setSafetyEnabled(False)
		self.rearRightMotor.setSafetyEnabled(False)
		
		self.stick = wpilib.Joystick(self.joystickChannel)
		self.auxiliary = wpilib.Joystick(1)
		
		
		
	def L_Test(self):
	  self.frontLeftMotor.set(.5)
	  self.frontRightMotor.set(0)
	  self.rearLeftMotor.set(.5)
	  self.rearRightMotor.set(0)
	
	
	
	def forward(self):
	  self.frontLeftMotor.set(.5)
	  self.frontRightMotor.set(.5)
	  self.rearLeftMotor.set(.5)
	  self.rearRightMotor.set(.5)
	def stop(self):
	  self.frontLeftMotor.set(0)
	  self.frontRightMotor.set(0)
	  self.rearLeftMotor.set(0)
	  self.rearRightMotor.set(0)
	
	def crab_right(self):
	  self.frontLeftMotor.set(.45)
	  self.rearLeftMotor.set(.2)
	  self.frontRightMotor.set(.45)
	  self.rearRightMotor.set(.2)
	  
	def crab_left(self):
	  self.frontLeftMotor.set(-.45)
	  self.rearLeftMotor.set(.2)
	  self.frontRightMotor.set(.45)
	  self.rearRightMotor.set(-.2)

	def autonomousInit(self):
		
		self.frontLeftMotor.setSafetyEnabled(False)
		self.frontRightMotor.setSafetyEnabled(False)
		self.rearLeftMotor.setSafetyEnabled(False)
		self.rearRightMotor.setSafetyEnabled(False)
		self.frontRightMotor.setQuadraturePosition(0,0)
		
		

	def autonomousPeriodic(self):
	
		#if True:
		self.frontLeftMotor.set(1)
		self.rearLeftMotor.set(1)
		self.frontRightMotor.set(1)
		self.rearRightMotor.set(1)
		# global step2 because it needs to know that the variable step2
		# that it is calling has already been assigned a number in the

		# goes forward to 10 feet if the robot has not gotten there yet

	def teleopInit(self):
		#Called when teleop starts; optional
		print("Starting team 753 Teleop")
		
		self.drive.setSafetyEnabled(False)
		
		self.frontRightMotor.setInverted(False)
		self.rearRightMotor.setInverted(False)
		self.frontLeftMotor.setInverted(False)
		self.rearLeftMotor.setInverted(False)
		
		self.frontRightMotor.setInverted(False)
		self.rearRightMotor.setInverted(False)
		print("hi")
		
	def teleopPeriodic(self):
		try:
			test = sd.getValue('adjust_x', 0)
			testy = sd.getValue('adjust_y', 0)
			testz = sd.getValue('adjust_z', 0)
			print('x ' + str(test))
			print('y ' + str(testy))
			print('z ' + str(testz))
		except Exception as e:
			print(str(e.args))
		
		"""if self.auxiliary.getRawButton(1):
			self.spinnyMotor.set(1)
		elif self.auxiliary.getRawButton(3):
			self.spinnyMotor.set(-1)
		elif self.auxiliary.getRawButton(6):
			self.spinnyMotor.set(.4)
		elif self.auxiliary.getRawButton(8):
			self.spinnyMotor.set(-.4)
		elif self.auxiliary.getRawButton(11):
			self.spinnyMotor.set(.7)
		else:
			self.spinnyMotor.set(0)"""



if __name__ == "__main__":
	wpilib.run(MyRobot)
