from control import TransferFunction, impulse_response
import matplotlib.pyplot as plt

G = TransferFunction([2], [1, 2])

inputs = [
    TransferFunction([1], [1, 0]),		# Ua
    TransferFunction([1], [1, 0, 4])	# Ub
]

sensors = [
    TransferFunction([4**2], [1, 2*0.5*4, 4**2]),   # S1
    TransferFunction([2**2], [1, 2*0.9*2, 2**2])	# S2
]

figure, axes = plt.subplots(len(inputs), len(sensors), figsize=(6, 4))

i = 0
for U in inputs:
    j = 0
    for S in sensors:
        Ym = S * G * U
        t, y = impulse_response(Ym)
        axes[i][j].plot(t, y)
        axes[i][j].set_xlabel("time")
        axes[i][j].set_ylabel("response")
        axes[i][j].set_title(f"U{i+1}, S{j+1}")
        j += 1
    i += 1

figure.tight_layout()
plt.savefig("q5.png")
plt.show()
