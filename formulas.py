import numpy as np

class Equations:
    def __init__(self, k, c, length, density):
        self.k = k
        self.c = c
        self.length = length
        self.density = density

    def thermal_conductivity(self):
        k_vector = (self.k/self.length)*np.array([[1, -1], [-1, 1]])
        return k_vector

    def thermal_capacity(self):
        c_vector = (self.length*self.c*self.density/2)*np.array([[1, -1], [-1, 1]])
        return c_vector

    def heat_flux_initial(self, T0, Ta):
        q1 = self.k/self.length*(T0 - Ta)
        q2 = -self.k / self.length * (T0 - Ta)
        return np.array([[q1], [q2]])

    def heat_flux(self, next_T, T, dt):
        new_q = self.c*((next_T-T/dt)) + self.k*T
        return new_q

    def next_temp(self, dt, q, T):
        T_next = (1/(self.c/dt + self.k))*(q+self.c*T)

        return T_next
