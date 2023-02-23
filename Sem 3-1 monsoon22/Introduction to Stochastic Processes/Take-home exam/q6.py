import sys
import numpy
import matplotlib.pyplot as plt
import random

ka = 1
kd = 1
a1 = 0.5
a0 = 0.05
b1 = 0.05
b0 = 0.01

def simulation(S):

    X1 = [400]
    X2 = [100] 
    Y = [0]
    t = [0]

    while t[-1] < int(sys.argv[1]):

        Rs = [ka * S * X1[-1], kd * X2[-1], a0 * X1[-1] + a1 * X2[-1], b0 * Y[-1] + b1 * Y[-1]]
        sumOfRates = sum(Rs)

        # ignore 0
        if sumOfRates == 0: break

        diff = numpy.random.exponential(1/sumOfRates)
        t.append(t[-1] + diff)

        r = random.uniform(0, 1)
        r *= sumOfRates

        if r <= Rs[0]:
            X1.append(X1[-1] - 1)
            X2.append(X2[-1] + 1)
            Y.append(Y[-1])
        elif r <= Rs[0] + Rs[1]:
            X1.append(X1[-1] + 1)
            X2.append(X2[-1] - 1)
            Y.append(Y[-1])
        elif r <= Rs[0] + Rs[1] + Rs[2]:
            X1.append(X1[-1])
            X2.append(X2[-1])
            Y.append(Y[-1] + 1)
        else:
            X1.append(X1[-1])
            X2.append(X2[-1])
            Y.append(Y[-1] - 1)

    return t, X1, X2, Y

for chosenS in range(1, 11):
    res_t, res_X1, res_X2, res_Y = simulation(chosenS)
    plt.plot(res_t, res_X1, label = "X_1")
    plt.plot(res_t, res_X2, label = "X_2")
    plt.plot(res_t, res_Y, label = "Y")
    plt.title(f"Simulation for S = {chosenS}")
    plt.xlabel("Time elapsed")
    plt.ylabel("Number of Particles")
    plt.savefig(f"S={chosenS}.png")
    plt.close()
    # plt.show()
