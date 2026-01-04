import numpy as np
import matplotlib.pyplot as plt

# Paramèètes du systèmes :

g = (-9.81) # m/s²
v_init = 14 # m/s
theta = 45 # °
h = 0 # m


# Axe du temps :
x = np.linspace(0, 17.85, 2000)


y = 0.5*g*(x/(v_init*np.cos(theta)))**2 + np.tan(theta)*x + h


# Légende de la deuxième courbe en LaTeX :
legende_graph = ("x(t)")


# Plot : Tracer le graphique
plt.figure()
plt.plot(x, y, label="x(t)", color="#f59e0b")
plt.xlabel("x (m)")
plt.ylabel("y(m)")
plt.title("Trajectoire de la pomme")
plt.grid(True)
plt.legend()
plt.show()
