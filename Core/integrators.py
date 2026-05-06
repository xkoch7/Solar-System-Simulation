import numpy as np
from Core.forces import compute_forces


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

def rk4_step(state, dt):
    s = state.copy()
    compute_forces(s)
    k1_velocity = s.acceleration
    k1_position = state.velocity

    s2 = state.copy()
    s2.position = state.position + k1_position * dt/2
    compute_forces(s2)
    k2_velocity = s2.acceleration
    k2_position = state.velocity + k1_velocity * dt/2

    s3 = state.copy()
    s3.position = state.position + k2_position * dt/2
    compute_forces(s3)
    k3_velocity = s3.acceleration
    k3_position = state.velocity + k2_velocity * dt/2

    s4 = state.copy()
    s4.position = state.position + k3_position * dt
    compute_forces(s4)
    k4_velocity = s4.acceleration
    k4_position = state.velocity + k3_velocity * dt

    state.position += (k1_position + 2*k2_position + 2*k3_position + k4_position) * dt/6
    state.velocity += (k1_velocity + 2*k2_velocity + 2*k3_velocity + k4_velocity) * dt/6
# coefficients for yoshida step

def yoshida_step(state, dt):
    # coefficients for yoshida step
    w1 = 1 / (2 - 2**(1/3))
    w0 = -2**(1/3) / (2 - 2**(1/3))
    c1 = c4 = w1 / 2
    c2 = c3 = (w0 + w1) / 2
    d1 = d3 = w1
    d2 = w0
    compute_forces(state)
    state.velocity += c1 * state.acceleration * dt
    state.position += d1 * state.velocity * dt
    compute_forces(state)
    state.velocity += c2 * state.acceleration * dt
    state.position += d2 * state.velocity * dt
    compute_forces(state)
    state.velocity += c3 * state.acceleration * dt
    state.position += d3 * state.velocity * dt
    compute_forces(state)
    state.velocity += c4 * state.acceleration * dt