import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:
    def __init__(self,linkName):
        self.linkName=linkName
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.values = np.zeros(c.num_iterations)

    def Get_Value(self,t):
        self.values[t]=pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        np.save("data/"+self.linkName+"SensorValues",self.values)