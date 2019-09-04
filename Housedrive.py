import math



class HouseDrive:
	'''
	this is the class for the housedrive system.
	Steering is handled by the front centered wheel
	'''
	def setup(self):
		self.leftMotorSpeed = 0
		self.rightMotorSpeed = 0
		self.frontSpeed = 0
		self.frontDirection = 0
		frontDriveMotor = self.rev.CANSparkMax(4,rev.MotorType(kBrushed))
		frontTurnMotor = self.rev.CANSparkMax(3,rev.MotorType(kBrushed))
		leftMotor = self.rev.CANSparkMax(2,rev.MotorType(kBrushed))
		rightMotor = self.rev.CANSparkMax(1,rev.MotorType(kBrushed))
		'''must change these ids later and get the length of the robot (halfYlength)'''
		
	def Execute(self, movements, direction):
		
		frontDriveMotor.set(filter(lambda x: 'fspeed' in x, movements)[0])
		frontTurnMotor.set(filter(lambda x: 'Fdirection' in x, movements)[0])
		leftMotor.set(filter(lambda x: 'left' in x, movements)[0])
		rightMotor.set(filter(lambda x: 'right' in x, movements)[0])
		
	def Get_Vectors(self,fwd,rot):
		
		self.frontSpeed = ((fwd**2) + (rot * self.halfYlength)**2)**0.5
		self.frontDirection = atan2(fwd,rot)
		self.leftMotorSpeed = fwd
		self.rightMotorSpeed = fwd
		
		
		movements = []
		movements.append([self.frontSpeed,'fspeed'],[self.frontDirection,'Fdirection'],[self.leftMotorSpeed,'left'],[self.rightMotorSpeed,'right'])
		movements.sort
		'''ensures the steering vector does not exceed the max speed 1'''
		if movements[0] > 1:
			scaledMovements = i[0]/(movements[0]) for i in movements
			Execute(self,scaledMovements,self.frontDirection)
		else:
			Execute(self,movements,self.frontDirection)
		
		
