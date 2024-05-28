import numpy as np

# plot the sample data
import matplotlib.pyplot as plt

# read the data with numpy
data = np.loadtxt('./Linescan_tests_Sensofar/full_line_high_res_1_um_demo_dh_c3_col1001.csv', delimiter=',')

# plot the data
plt.plot(data[:,0], data[:,1], label='Profile 1')
plt.xlabel('Distance [um]')
plt.ylabel('Height [um]')
plt.show()