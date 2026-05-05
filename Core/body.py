import numpy as np
from dataclasses import dataclass

@dataclass
class SystemState:
        names: list[str]
        mass: np.ndarray
        velocity: np.ndarray
        position: np.ndarray
        acceleration: np.ndarray

        @classmethod
        def create(cls, mass, velocity, names, position):
            mass = np.array(mass , dtype=np.float64)
            velocity = np.array(velocity , dtype=np.float64)
            names = names
            position = np.array(position , dtype=np.float64)
            acceleration = np.zeros(position.shape)
            return cls(names=names, mass=mass, position=position, velocity=velocity, acceleration=acceleration)
        def copy(self):
              return SystemState.create(
                    mass = self.mass.copy(),
                    velocity = self.velocity.copy(),
                    names = self.names.copy(),
                    position = self.position.copy()
            )
