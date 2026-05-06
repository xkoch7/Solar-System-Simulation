from Core.body import SystemState
from Core.forces import compute_forces
from Core.integrators import euler_step, leapfrog_step, rk4_step, yoshida_step
from Core.simulation import Simulation
from Analysis.diagnostics import total_energy

# create two identical states — one for euler, one for leapfrog
state_euler = SystemState.create(
    mass=[1e30, 1e30],
    position=[[-1e11, 0, 0], [1e11, 0, 0]],
    velocity=[[0, 1e4, 0], [0, -1e4, 0]],
    names=['A', 'B']
)
state_leapfrog = state_euler.copy()
state_rk4 = state_euler.copy()
state_yoshida = state_euler.copy()
# record energy before
KE, PE = total_energy(state_euler)
e0_euler = KE + PE
KE, PE = total_energy(state_leapfrog)
e0_leapfrog = KE + PE
KE, PE = total_energy(state_rk4)
e0_rk4 = KE + PE
KE, PE = total_energy(state_yoshida)
e0_yoshida = KE + PE

# create simulations and run
sim_euler = Simulation(state=state_euler, dt=500000, integrator=euler_step)
sim_leapfrog = Simulation(state=state_leapfrog, dt=500000, integrator=leapfrog_step)
sim_rk4 = Simulation(state=state_rk4, dt = 500000, integrator=rk4_step)
sim_yoshida = Simulation(state=state_yoshida, dt = 500000, integrator=yoshida_step)

sim_euler.run(1000)
sim_leapfrog.run(1000)
sim_rk4.run(1000)
sim_yoshida.run(1000)

# record energy after
KE, PE = total_energy(state_euler)
e1_euler = KE + PE
KE, PE = total_energy(state_leapfrog)
e1_leapfrog = KE + PE
KE, PE = total_energy(state_rk4)
e1_rk4 = KE + PE
KE, PE = total_energy(state_yoshida)
e1_yoshida = KE + PE

# print drift ratio
print(f"Euler energy drift:    {(e1_euler - e0_euler) / abs(e0_euler):.6f}")
print(f"Leapfrog energy drift: {(e1_leapfrog - e0_leapfrog) / abs(e0_leapfrog):.6f}")
print(f"rk4 energy drift: {(e1_rk4 - e0_rk4) / abs(e0_rk4):.6f}")
print(f"yoshida energy drift: {(e1_yoshida - e0_yoshida) / abs(e0_yoshida):.6f}")