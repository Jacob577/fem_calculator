import numpy as np
from formulas import Equations

T0 = 40
Ta = 20
dt = 1
T_vector = [[T0], [Ta]]
k = 1.5
length = 0.5
c = 900
density = 2300


class Main:
    def __init__(self):
        self.eq = Equations(k=k, c=c, length=length, density=density)
        # self.k = self.eq.thermal_conductivity()
        # self.c = self.eq.thermal_capacity()
        # self.q = self.eq.heat_flux_initial(T0=T0, Ta=Ta)
        # self.T = np.array([[T0], [Ta]])

    def calculate_temps(self):
        k_global = self.eq.global_conductivity(3)
        c_global = self.eq.global_capacity(3, density)
        T_global = np.array([[500], [20], [20], [20]])
        q_global, T_global = self.eq.global_flux(
            k_global=k_global, c_global=c_global, T_global=T_global, dt=dt, q_global=1
        )
        count = 1
        for i in range(300):
            count =+ 1
            q_global, T_global = self.eq.global_flux(
                k_global=k_global, c_global=c_global, T_global=T_global, dt=dt, q_global=q_global
            )
        print(T_global)
        # print(k_global)
        # print(q_global)
        # print(T_global)
        # print(q_global)

if __name__ == "__main__":
    Main().calculate_temps()
