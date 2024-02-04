import numpy as np
import matplotlib.pyplot as plt

backLegSensorValues=np.load('data/backLegSensorValues.npy')
FrontLegSensorValues=np.load('data/FrontLegSensorValues.npy')

plt.plot(backLegSensorValues,label="Back Leg",linewidth=3)
plt.plot(FrontLegSensorValues,label="Front Leg")

#making sine wave
# num_iterations = 1000
# time = np.linspace(0, 2 * np.pi, num_iterations)
# targetAngles = np.sin(time)
# targetAngles = np.interp(targetAngles, (targetAngles.min(), targetAngles.max()), (-np.pi/4, np.pi/4))
# np.savetxt('targetAngles.txt', targetAngles)
plt.plot(targetAngles)

plt.legend()
plt.show()