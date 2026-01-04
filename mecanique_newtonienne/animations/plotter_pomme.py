import numpy as np
import matplotlib.pyplot as plt

# =========================
# Constante physique
# =========================
g = -9.81  # m/s²

# Axe horizontal (distance)
x = np.linspace(0, 35, 2000)

# =========================
# Création du canvas
# =========================
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# ==================================================
# 1️⃣ Variation de la vitesse initiale
# v_init de 6 à 18 m/s
# h = 0 m, theta = 45°
# ==================================================
theta = np.deg2rad(45)
h = 0

for v_init in range(6, 19, 2):
    y = 0.5 * g * (x / (v_init * np.cos(theta)))**2 + np.tan(theta) * x + h
    axes[0].plot(x, y, label=f"{v_init} m/s")

axes[0].set_title("Variation de la vitesse initiale")
axes[0].set_xlabel("x (m)")
axes[0].set_ylabel("y (m)")
axes[0].grid(True)
axes[0].legend()


# ==================================================
# 2️⃣ Variation de l’angle
# theta de 15° à 75°
# h = 0 m, v_init = 14 m/s
# ==================================================
v_init = 14
h = 0

for theta_deg in range(15, 76, 15):
    theta = np.deg2rad(theta_deg)
    y = 0.5 * g * (x / (v_init * np.cos(theta)))**2 + np.tan(theta) * x + h
    axes[1].plot(x, y, label=f"{theta_deg}°")

axes[1].set_title("Variation de l’angle de tir")
axes[1].set_xlabel("x (m)")
axes[1].grid(True)
axes[1].legend()


# ==================================================
# 3️⃣ Variation de la hauteur initiale
# h de 0 à 10 m
# v_init = 14 m/s, theta = 45°
# ==================================================
v_init = 14
theta = np.deg2rad(45)

for h in range(0, 11, 2):
    y = 0.5 * g * (x / (v_init * np.cos(theta)))**2 + np.tan(theta) * x + h
    axes[2].plot(x, y, label=f"h = {h} m")

axes[2].set_title("Variation de la hauteur initiale")
axes[2].set_xlabel("x (m)")
axes[2].grid(True)
axes[2].legend()


# =========================
# Mise en forme globale
# =========================
plt.suptitle("Étude de la trajectoire d’un projectile", fontsize=16)
plt.tight_layout()

# Suppression des graduations négatives
for ax in axes:
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)

plt.show()
