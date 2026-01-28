import numpy as np
import matplotlib.pyplot as plt

# =========================
# PARÁMETROS
# =========================
L = 10        # longitud de la escalera
xp = 2        # x' = dx/dt (constante)
dt = 0.05

t_max = L / xp - 0.05
t = np.arange(0, t_max, dt)

x = xp * t
y = np.sqrt(L**2 - x**2)

# =========================
# FIGURA
# =========================
plt.ion()
fig, ax = plt.subplots(figsize=(6, 6))

ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
ax.set_aspect("equal")
ax.set_title("Deslizamiento de la escalera")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.grid(True)

ladder, = ax.plot([], [], lw=3, color="red")
base, = ax.plot([], [], "bo")
top, = ax.plot([], [], "go")

fig.show()
plt.pause(0.1)

# =========================
# ANIMACIÓN
# =========================
for i in range(len(t)):
    ladder.set_data([0, x[i]], [y[i], 0])
    base.set_data([x[i]], [0])
    top.set_data([0], [y[i]])

    plt.pause(0.05)

plt.ioff()
plt.show()
