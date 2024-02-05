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


##############################
#making sine wave
amplitudeF = np.pi/8
frequencyF = 10
phaseOffsetF = 0

amplitudeB = np.pi/8
frequencyB = 10
phaseOffsetB = np.pi/2

num_iterations = 1000

timing = np.linspace(0, 2 * np.pi, num_iterations)
targetAnglesF = amplitudeF * np.sin(frequencyF * timing + phaseOffsetF)
targetAnglesF = np.interp(targetAnglesF, (targetAnglesF.min(), targetAnglesF.max()), (-np.pi/4, np.pi/4))
np.savetxt('targetAnglesF.txt', targetAnglesF)
targetAnglesB = amplitudeB * np.sin(frequencyB* timing + phaseOffsetB)
targetAnglesB = np.interp(targetAnglesB, (targetAnglesB.min(), targetAnglesB.max()), (-np.pi/4, np.pi/4))
np.savetxt('targetAnglesB.txt', targetAnglesB)
##############################

for i in range(1000):
    time.sleep(1/240)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
                                jointName = "Torso_BackLeg",
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = targetAnglesB[i],
                                maxForce = 35)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,
                                jointName = "Torso_FrontLeg",
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = targetAnglesF[i],
                                maxForce = 35)

p.disconnect()
np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy",frontLegSensorValues)