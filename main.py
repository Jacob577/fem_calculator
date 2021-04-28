import numpy as np
from formulas import Equations
import matplotlib
import matplotlib.pyplot as plt

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
        T_global = np.array([[20], [20], [20], [20]])
        q_global, T_global = self.eq.global_flux(
            k_global=k_global, c_global=c_global, T_global=T_global, dt=dt, q_global=1
        )
        count1 = [20]
        count2 = [0]
        for i in range(1000):
            q_global, T_global = self.eq.global_flux(
                k_global=k_global, c_global=c_global, T_global=T_global, dt=dt, q_global=q_global
            )
            count1 += [T_global[0][0]]
            count2 += [count2[-1]+1]
        # print(q_obal)
        # print(k_global)
        # print(q_global)
        # print(T_global)
        # print(q_global)
        # plt.plot(count2, count1)
        # plt.show()
        # print(count2)

if __name__ == "__main__":
    Main().calculate_temps()
