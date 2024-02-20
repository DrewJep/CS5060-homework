import numpy as np

gravity = -9.8
maxForce = 35


sleep_time = 1/360
num_iterations = 1000

amplitudeF = np.pi/8
frequencyF = 10
phaseOffsetF = 0

amplitudeB = np.pi/8
frequencyB = 10
phaseOffsetB = np.pi/2

numberOfGenerations =  10
populationSize = 10

numSensorNeurons = 4
numMotorNeurons = 8

motorJointRange = 0.5