import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math
from random import *
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

B = 1 / 1836  # Tesla
Omega = 2.6  # circular frequency (1/sec)
R = 5.6875  # helical radius (meter)
time = 10  # time of simulation (sec)
time_step = 0.01  # duration of each step (sec)

# Array lists
particles = np.zeros((2,), dtype=[('x', 'float'), ('y', 'float'), ('z', 'float'), ('vx', 'float'), ('vy', 'float'),
                                  ('vz', 'float')])

particles[0]['x'] = 0
particles[0]['y'] = 1
particles[0]['z'] = 0
particles[0]['vx'] = 1
particles[0]['vy'] = 0
particles[0]['vz'] = 1

particles[1]['x'] = 0
particles[1]['y'] = -1
particles[1]['z'] = 0
particles[1]['vx'] = 1
particles[1]['vy'] = 0
particles[1]['vz'] = 1


def distance_between_particles(count, xp, yp, zp, xe, ye, ze):
    x1 = xp[count]
    x2 = xe[count]
    y1 = yp[count]
    y2 = ye[count]
    z1 = zp[count]
    z2 = ze[count]
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) + (z1 - z2) * (z1 - z2))


def simulate_for_electron(index=1):
    curr_time = 0
    x = [particles[index]['x']]
    y = [particles[index]['y']]
    z = [particles[index]['z']]
    omega = Omega
    while curr_time < time:
        curr_time += time_step
        particles[index]['x'] += (particles[index]['vx']) * math.cos(omega * curr_time)
        particles[index]['y'] += (particles[index]['vx']) * math.sin(omega * curr_time)
        particles[index]['z'] = (particles[index]['vz'] * curr_time)
        x.append(particles[index]['x'])
        y.append(particles[index]['y'])
        z.append(particles[index]['z'])
    return x, y, z


def simulate_for_proton(index=0):
    curr_time = 0
    x = [particles[index]['x']]
    y = [particles[index]['y']]
    z = [particles[index]['z']]
    omega = Omega
    while curr_time < time:
        curr_time += time_step

        particles[index]['x'] += (particles[index]['vx']) * math.cos(omega * curr_time)
        particles[index]['y'] += (particles[index]['vx']) * math.sin(omega * curr_time)
        particles[index]['z'] = (particles[index]['vz'] * curr_time)

        x.append(particles[index]['x'])
        y.append(particles[index]['y'])
        z.append(particles[index]['z'])
    return x, y, z


def simulate_two_particles():
    curr_time = 0
    xp = [particles[0]['x']]
    yp = [particles[0]['y']]
    zp = [particles[0]['z']]
    xe = [particles[1]['x']]
    ye = [particles[1]['y']]
    ze = [particles[1]['z']]
    omega = Omega
    count = 0
    while curr_time < time:
        curr_time += time_step
        if distance_between_particles(count, xp, yp, zp, xe, ye, ze) < 2 * R:
            omega += 0.1

        xp.append(xp[count] + (particles[0]['vx']) * math.cos(-Omega * curr_time))
        yp.append(yp[count] + (particles[0]['vx']) * math.sin(-Omega * curr_time))
        zp.append(particles[0]['vz'] * curr_time)

        xe.append(xe[count] + (particles[1]['vx']) / 2 * math.cos(omega * curr_time))
        ye.append(ye[count] + (particles[1]['vx']) / 2 * math.sin(omega * curr_time))
        ze.append((particles[1]['vz']) * curr_time)
        count += 1
    return xp, yp, zp, xe, ye, ze


def func(num, dataSet, line):
    line.set_data(dataSet[0:2, :num])
    line.set_3d_properties(dataSet[2, :num])

    return line


def main():
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    # xe, ye, ze = simulate_for_electron()
    # xp, yp, zp = simulate_for_proton()
    xp, yp, zp, xe, ye, ze = simulate_two_particles()
    dataSet = np.array([xe, ye, ze])
    line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0]
    dataSet = np.array([xp, yp, zp])
    line = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, c='g')[0]
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Joint motion of a proton and an electron')

    anim = animation.FuncAnimation(fig, func, frames=len(ze), fargs=(dataSet, line), interval=20,
    blit=False, repeat=True)
    #anim.save('file2.gif', fps=60)
    plt.show()
    plt.savefig('particle1.png')


main()
