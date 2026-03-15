import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

# Number of points on the circle
N = 12
multiplier = 5

#Angle positions
angles = np.linspace(0,2*np.pi , N , endpoint=False)

#figure setup 
fig, ax =plt.subplots(figsize=(6,6))
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('black')

lines = []

#Draw initial lines
for i in range(N):
    j=(i*multiplier) % N
    line, = ax.plot(
        [np.cos(angles[i]), np.cos(angles[j])],
        [np.sin(angles[i]), np.sin(angles[j])],
        color=plt.cm.hsv(i / N),
        alpha=0.4 ,
        linewidth=1
    )
    lines.append(line)
#Circle outline
circle = plt.Circle((0,0),1, color='white' , fill=False , alpha=0.2)
ax.add_artist(circle)
ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)

#Animation function
def update(frame):
    rot = frame * 0.01  #rotation speed
    for i, line in enumerate(lines):
        j = (i* multiplier) % N

        x1 = np.cos(angles[i] + rot)
        y1 = np.sin(angles[i] + rot)
        x2 = np.cos(angles[j] + rot)
        y2 = np.sin(angles[j] + rot)

        line.set_data([x1 , x2] , [y1 , y2])
    return lines

#Animate
ani = FuncAnimation(fig, update , frames=360 , interval=30)
plt.show()

