import numpy as np

G = 6.674e-11

def total_energy(state):
    Potential_energy = 0.0
    for i in range(len(state.mass)):
        for j in range(i + 1, len(state.mass)):
            distance = np.linalg.norm(state.position[j] - state.position[i])
            Potential_energy += (-G * state.mass[i] * state.mass[j]) / distance
    Kinetic_energy = 0.5 * np.sum(state.mass * np.sum(state.velocity ** 2, axis=1))
    return Kinetic_energy, Potential_energy
    
def total_momentum(state):
    return np.sum(state.mass[:, np.newaxis] * state.velocity, axis=0)

