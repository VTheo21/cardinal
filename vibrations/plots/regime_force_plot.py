import numpy as np
import matplotlib.pyplot as plt


# Paramètres du système :
m = 7
k = 100
c = 10


w0 = np.sqrt(k/m)                            # ω0 (pulsation propre) en rad/s
zeta = c / (2*np.sqrt(k*m))                       # ζ (coefficient d’amortissement)
wd = w0 * np.sqrt(1 - zeta**2)    # ωd = ω0 * sqrt(1-ζ²) (cas sous-amorti ζ<1)
w = 1
F = 2

Up = (F / k) / np.sqrt((1 - (w / w0)**2)**2 + (2 * zeta * w / w0)**2)
phi = np.arctan((2 * zeta * (w / w0)) / (1 - (w / w0)**2))


# Conditions initiales :
u0 = 1.0          # u(0)
u0_dot = 0.0      # u'(0)


# Axe du temps :
t = np.linspace(0, 10, 2000)


# Équation : u(t)

A = u0 - Up * np.cos(phi)
B = (u0_dot + zeta * w0 * u0 - Up * (zeta * w0 * np.cos(phi) + w * np.sin(phi))) / wd

u = np.exp(-zeta * w0 * t) * ( A * np.cos(wd * t) + B * np.sin(wd * t)) + Up * np.cos(w*t-phi)
u_amplitude = np.exp(-zeta * w0 * t) * np.sqrt((u0 - Up * np.cos(phi))**2 + ((u0_dot + zeta * w0 * u0 - Up * (zeta * w0 * np.cos(phi) + w * np.sin(phi))) / wd)**2)


# Légende de la deuxième courbe en LaTeX :
legende_graph = ("|u_h(t)|")


# Plot : Tracer le graphique
plt.figure()
plt.plot(t, u, label="u(t)", color="#f59e0b")
plt.plot(t, u_amplitude, linestyle="--", linewidth = 1, alpha = 0.5, color="gray", label=legende_graph)
plt.plot(t, -u_amplitude, linestyle="--", linewidth = 1, alpha = 0.5, color="gray")
plt.xlabel("t (s)")
plt.ylabel("u(t)")
plt.title("Réponse u(t)")
plt.grid(True)
plt.legend()
plt.show()
