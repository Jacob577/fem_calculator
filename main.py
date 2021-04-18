import numpy as np
from formulas import Equations

T0 = 600
Ta = 20
dt = 0.01
T_vector = [[T0], [Ta]]
k = 1.5
length = 0.05
c = 900
density = 2300

class Main:

    def __init__(self):
        self.eq = Equations(k=k, c=c, length=length, density=density)
        self.k = self.eq.thermal_conductivity()
        self.c = self.eq.thermal_capacity()
        self.q = self.eq.heat_flux_initial(T0=T0, Ta=Ta)
        self.T = np.array([[T0], [Ta]])

    def calculate_temps(self):
        for i in range(10):
            next_T = self.eq.next_temp(dt=dt, q=self.q, T=self.T)
            self.q = self.eq.heat_flux(next_T=next_T, T=self.T, dt=dt)
            self.T = next_T
            self.T[0] = T0

            # print(self.q)
            print(self.T)
            print('\n')


if __name__ == "__main__":
    Main().calculate_temps()
