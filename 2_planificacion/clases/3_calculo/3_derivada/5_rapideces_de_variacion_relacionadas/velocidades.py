import numpy as np
import matplotlib.pyplot as plt

# =========================
# PARÁMETROS
# =========================
L = 10
xp = 2
dt = 0.05

t_max = L / xp - 0.05
t = np.arange(0, t_max, dt)

x = xp * t
y = np.sqrt(L**2 - x**2)

# Velocidad vertical (modelo implícito)
yp = -(x / y) * xp

# =========================
# FIGURA
# =========================
plt.ion()
fig, ax = plt.subplots(figsize=(7, 4))

ax.set_xlim(0, t[-1])
ax.set_ylim(-6, 3)
ax.set_title("Velocidades vs tiempo")
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Velocidad (m/s)")
ax.grid(True)

vx_line, = ax.plot([], [], label="x'(t) constante", color="blue")
vy_line, = ax.plot([], [], label="y'(t) variable", color="green")
ax.legend()

fig.show()
plt.pause(0.1)

# =========================
# TRAZADO PROGRESIVO
# =========================
for i in range(len(t)):
    vx_line.set_data(t[:i+1], np.full(i+1, xp))
    vy_line.set_data(t[:i+1], yp[:i+1])

    plt.pause(0.05)

plt.ioff()
plt.show()
