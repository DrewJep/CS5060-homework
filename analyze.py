import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues=np.load('data/backLegSensorValues.npy')
FrontLegSensorValues=np.load('data/FrontLegSensorValues.npy')

plt.plot(backLegSensorValues,label="Back Leg",linewidth=3)
plt.plot(FrontLegSensorValues,label="Front Leg")

plt.legend()
plt.show()