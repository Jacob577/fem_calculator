import numpy as np

class Equations:
    def __init__(self, k, c, length, density):
        self.k = k
        self.c = c
        self.length = length
        self.density = density

    # def thermal_conductivity(self):
    #     k_vector = (self.k/self.length)*np.array([[1, -1], [-1, 1]])
    #     return k_vector
    #
    # def thermal_capacity(self):
    #     c_vector = (self.length*self.c*self.density/2)*np.array([[1, -1], [-1, 1]])
    #     return c_vector
    #
    # def heat_flux_initial(self, T0, Ta):
    #     q1 = self.k/self.length*(T0 - Ta)
    #     q2 = self.k / self.length*(Ta - T0)
    #     return np.array([[q1], [q2]])
    #
    # def heat_flux(self, next_T, T, dt):
    #     new_q = self.c*((next_T-T)/dt) + self.k*T
    #     return new_q
    #
    # def next_temp(self, dt, q, T):
    #     T_next = (1/(self.c/dt + self.k))*(q+self.c*T)
    #     # T_next = T + ((dt * self.c)**(-1)) * (q - self.k * T)
    #
    #     return T_next

    def global_conductivity(self, elements):
        if elements == 1:
            k_global = np.array([[self.k, self.k], [self.k, self.k]])
        else:
            k_global = np.zeros([elements + 1, elements + 1])
            k_global[0][0] = self.k

            for i in range(elements + 1):
                for j in range(elements + 1):
                    if (j == i) and (i != 0 and i != elements + 1):
                        k_global[i][j] = self.k*2
                    elif (i == j+1) or (i == j-1):
                        try:
                            k_global[i][j] = self.k
                        except:
                            k_global = k_global
            k_global[elements][elements] = self.k
        return k_global

    def global_capacity(self, elements, density):
        c = self.length * self.c * density / 2
        if elements == 1:
            c_global = np.array([[c, 0], [0, c]])
        else:
            c_global = np.zeros([elements + 1, elements + 1])
            c_global[0][0] = c

            for i in range(elements + 1):
                for j in range(elements + 1):
                    if (j == i) and (i != 0 and i != elements + 1):
                        c_global[i][j] = c*2
                    elif (i == j+1) or (i == j-1):
                        try:
                            c_global[i][j] = c
                        except:
                            c_global = c_global
            c_global[elements][elements] = c
        return c_global

    def global_flux(self, k_global, c_global, T_global, dt, q_global):
        if type(q_global) == int:
            q_global = k_global*T_global
            q_global[0][0] = 1000000
            next_temp = T_global + (1/(dt*c_global))*(q_global - k_global*T_global)
            dT = (next_temp - T_global) / dt
            # print(next_temp)
        else:
            q_global[0][0] = 1000000
            next_temp = T_global + dt*(1/c_global)*(q_global-k_global*T_global)
            # dT = np.zeros([len(T_global + 1), len(T_global + 1)])
            dT = (next_temp - T_global) / dt
            # for i in range(len(T_global + 1)):
            #     if i != 0 and i != len(T_global):
            #         dT[i][i] = (next_temp[i-1][i-1] + next_temp[i][i])/dt
            #     elif i == len(T_global):
            #         dT[-1][-1] = (next_temp[i-1][i-1] + 20)/2

            # dT = (next_temp - T_global)/dt
            q_global = k_global*next_temp + c_global*dT
            print(dT)
            print('\n')

        return q_global, next_temp




