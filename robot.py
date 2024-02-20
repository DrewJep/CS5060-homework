from motor import MOTOR
from sensor import SENSOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pyrosim.pyrosim as pyrosim
import pybullet as p
import os
import constants as c

class ROBOT:
    def __init__(self,solutionID):
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system(f"rm brain{solutionID}.nndf")
    
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
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()
    
    def Get_Fitness(self,id):
        f = open(f"data/tmp{id}.txt", "w")
        f.write(str(p.getLinkState(self.robotId, 0)[0][0]))
        f.close()
        os.system(f"mv data/tmp{id}.txt data/fitness{id}.txt")