import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import numpy as np
import random as rand

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

with open('targetAngles.txt', 'r') as file:
    targetAngles_list = [float(line.strip()) for line in file]

for i in range(1000):
    time.sleep(1/1000)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
                                jointName = "Torso_BackLeg",
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = targetAngles_list[i],
                                maxForce = 35)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
                                jointName = "Torso_FrontLeg",
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = targetAngles_list[i],
                                maxForce = 35)

p.disconnect()
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy",frontLegSensorValues)