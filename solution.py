import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random as rand
import time
import constants as c

length=1
width=1
height=1
x=0
y=0
z=.5

class SOLUTION:
    def __init__(self,id):
        self.myID = id
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1

    def Set_ID(self, id):
        self.myID = id
    
    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"python3 simulate.py {directOrGUI} {self.myID} 2&>1 &")
        while not os.path.exists(f"data/fitness{self.myID}.txt"):
            time.sleep(0.01)
        f = open(f"data/fitness{self.myID}.txt", "r")
        self.fitness = float(f.read())
        f.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"python3 simulate.py {directOrGUI} {self.myID} 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists(f"data/fitness{self.myID}.txt"):
            time.sleep(0.01)
        f = open(f"data/fitness{self.myID}.txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system(f"rm data/fitness{self.myID}.txt")

    def Mutate(self):
        self.weights[rand.randint(0, c.numSensorNeurons-1)][rand.randint(0, c.numMotorNeurons-1)] = rand.random()*2 - 1
    
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-5, 5, 0.5] , size=[1,1,1])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1, 1, 1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg",
                            type = "revolute", position = [0,0.5,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[.25, 1, .25])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg",
                            type = "revolute", position = [0,-0.5,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[.25, 1, .25])

        pyrosim.End()
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron(name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4 , jointName = "Torso_FrontLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentCol in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, 
                                     targetNeuronName = currentCol + c.numSensorNeurons, 
                                     weight = self.weights[currentRow][currentCol])
        pyrosim.End()
