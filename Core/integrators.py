import numpy as np
from forces import compute_forces


def euler_step(state, dt):
    compute_forces(state)
    state.velocity += state.acceleration * dt
    state.position += state.velocity * dt

def leapfrog_step(state, dt):
    compute_forces(state)
    state.velocity += state.acceleration * (dt / 2)   
    state.position += state.velocity * dt
    compute_forces(state)
    state.velocity += state.acceleration * (dt / 2)  