from motor import MOTOR
from sensor import SENSOR
import pyrosim.pyrosim as pyrosim
import pybullet as p

class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        

    def Prepare_To_Sense(self):
        self.sensors={}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        self.motors={}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Sense(self,t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)
    
    def Act(self,t):
        for motor in self.motors.values():
            motor.Set_Value(self.robotId,t)