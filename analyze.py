import numpy as np
import matplotlib.pyplot as plt

# backLegSensorValues=np.load('data/backLegSensorValues.npy')
# FrontLegSensorValues=np.load('data/FrontLegSensorValues.npy')

# plt.plot(backLegSensorValues,label="Back Leg",linewidth=3)
# plt.plot(FrontLegSensorValues,label="Front Leg")


with open('targetAnglesF.txt', 'r') as file:
    targetAnglesF = [float(line.strip()) for line in file]
with open('targetAnglesB.txt', 'r') as file:
    targetAnglesB = [float(line.strip()) for line in file]

plt.plot(targetAnglesF,label="Front Leg")
plt.plot(targetAnglesB,label="Back Leg")

plt.legend()
plt.show()