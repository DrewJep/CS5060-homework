from world import WORLD
from robot import ROBOT
import constants as c
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time


class SIMULATION:
    def __init__(self,directOrGUI):
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity)
        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.num_iterations):
            time.sleep(c.sleep_time)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
