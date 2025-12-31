import numpy as np
import matplotlib.pyplot as plt


# Paramètres du système :
w0 = 5                            # ω0 (pulsation propre) en rad/s
zeta = 0.15                       # ζ (coefficient d’amortissement)
wd = w0 * np.sqrt(1 - zeta**2)    # ωd = ω0 * sqrt(1-ζ²) (cas sous-amorti ζ<1)


# Conditions initiales :
u0 = 1.0          # u(0)
u0_dot = 0.0      # u'(0)


# Axe du temps :
t = np.linspace(0, 10, 2000)


# Équation : u(t) = exp(-ζ ω0 t)[ u0 cos(ωd t) + (u'(0)+ζ ω0 u0)/ωd * sin(ωd t) ]
u = np.exp(-zeta * w0 * t) * ( u0 * np.cos(wd * t) + ((u0_dot + zeta * w0 * u0) / wd) * np.sin(wd * t))
u_amplitude = np.exp(-zeta * w0 * t) * np.sqrt(u0**2 + ((zeta * w0 * u0 + u0_dot) / wd)**2)


# Légende de la deuxième courbe en LaTeX :
legende_graph = (r"$e^{-\zeta \omega_0 t}"r"\sqrt{u_0^2 + \left(\frac{\zeta \omega_0 u_0 + \dot{u}_0}{\omega_d}\right)^2}$")


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
