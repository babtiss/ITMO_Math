# import library's
from vpython import *
import math
import numpy as np
import matplotlib.pyplot as plt

# initial constants
Q_ELECTRON = 1.6e-19
KE = 1e5 * Q_ELECTRON  # eV*conversion factor in J
KEL = 9e9  # kinetic energy of the alpha particles in J
N_GOLD = 79
MASS = 4 * 1.67e-27

# initial utils
SCALE = 1e-10
DT = 1e-19
scene = canvas(title='Rutherford Scattering', background=color.white)
run = True
R = SCALE
RANGE_OF_PARTICLES = arange(-0.20 * SCALE, SCALE * 0.20, SCALE * 0.009)
vx = []
vy = []
yi = []
theta = []
alphas = []

# create particles
gold = sphere(color=color.black, radius=0.01 * SCALE)
gold.charge = N_GOLD * Q_ELECTRON

for i in RANGE_OF_PARTICLES:
    particle = sphere(color=color.black, radius=0.001 * R, stop=False)
    attach_trail(particle, radius=0.001 * R, color=color.black)
    particle.mass = MASS
    particle.charge = 2 * Q_ELECTRON
    particle.pos = vec(-0.6 * SCALE, i, 0)
    yi.append(particle.pos.y)
    particle.mom = sqrt(2 * particle.mass * KE) * vec(1, 0, 0)      # instantaneous position of a particle
    alphas.append(particle)

# run simulation
while run:
    rate(20)
    for particle in alphas:
        if not particle.stop:
            runit = particle.pos / mag(particle.pos)
            F = KEL * particle.charge * gold.charge / mag2(particle.pos) * runit  # particle deflection calculation
            particle.mom = particle.mom + F * DT
            particle.pos = particle.pos + (particle.mom / particle.mass) * DT
        if mag(particle.pos) > SCALE * 0.7:
            particle.stop = True
            run = False


def ang(cx, cy):
    # scattering angle
    if (abs(cx) == 0) and (cy > 0):
        return np.pi / 2
    elif (abs(cx) == 0) and (cy < 0):
        return 3 * np.pi / 2
    elif (abs(cx) == cx) and (abs(cy) == cy):  # first
        return (np.pi / 2) - math.atan2(cx, cy)
    elif (abs(cx) == -cx) and (abs(cy) == cy):  # second
        return (np.pi / 2) - math.atan2(cx, cy)
    elif (abs(cx) == -cx) and (abs(cy) == -cy):  # third
        return (-np.pi / 2) - (np.pi + math.atan2(cx, cy))
    elif (abs(cx) == cx) and (abs(cy) == -cy):  # fourth
        return -math.atan2(cx, cy) + np.pi / 2
    else:
        return 0


for particle in alphas:
    vx.append(particle.mom.x)
    vy.append(particle.mom.y)
    theta.append(ang(particle.pos.x, particle.pos.y) * 180 / np.pi)

# create plot

plt.scatter(yi, theta)
plt.xlabel('Incident Position')
plt.ylabel('Scattering Angle')
plt.title('Incident Position vs. Scattering Angle')
