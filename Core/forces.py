import numpy as np
from Core.body import SystemState
#constants
G = 6.674e-11
SOFTENING = 1e7

#function to compute forces between celestial bodies
def compute_forces(state):
    state.acceleration.fill(0)
    for i in range(len(state.mass)):
        for j in range(i + 1, len(state.mass)):
            r = state.position[j] - state.position[i]
            distance = (np.dot(r, r) + SOFTENING**2) ** 1.5
            state.acceleration[i] += G * state.mass[j] * r / distance
            state.acceleration[j] -= G * state.mass[i] * r / distance