from body import SystemState

class Simulation:
    def __init__ (self, state, dt, integrator):
        self.state = state
        self.dt = dt
        self.integrator = integrator
        self.history = []
    def step(self):
        self.integrator(self.state, self.dt)
    def run(self, steps):
        for i in range(steps):
            self.history.append(self.state.position.copy())
            self.step()
