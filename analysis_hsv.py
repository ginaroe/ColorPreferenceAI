import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

df = pd.read_csv('pretty_yes_hsv.csv')
H = df['H']
S = df['S']
V = df['V']

df2 = pd.read_csv('pretty_no_hsv.csv')
X = df2['H']
Y = df2['S']
Z = df2['V']

ax.set_title("Distribution of non/Pretty Colors")
ax.scatter(H, S, V) #blue
ax.scatter(X, Y, Z) #yellow
ax.set_xlabel('Hue')
ax.set_ylabel('Saturation')
ax.set_zlabel('Value')
ax.legend("PN")
plt.show()