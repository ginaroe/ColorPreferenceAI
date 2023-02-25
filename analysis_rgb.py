import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

df = pd.read_csv('pretty_yes.csv')
R = df['R']
G = df['G']
B = df['B']

df2 = pd.read_csv('pretty_no.csv')
X = df2['R']
Y = df2['G']
Z = df2['B']

ax.set_title("Distribution of non/Pretty Colors")
ax.scatter(R, G, B) #blue
ax.scatter(X, Y, Z) #yellow
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')
ax.legend("PN")
plt.show()