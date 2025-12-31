import numpy as np
import matplotlib.pyplot as plt

# Définition de l'axe x
x = np.linspace(-20, 20, 1000)

# Sinus cardinal (gestion de x = 0)
y = np.sinc(x / np.pi)  # np.sinc(t) = sin(pi*t)/(pi*t)

# Création de la figure
plt.figure(figsize=(8, 4), dpi=300, facecolor='white')

# Tracé de la courbe
plt.plot(x, y, color='#6fa8dc', linewidth=8)

# Fond blanc et nettoyage du graphique
plt.gca().set_facecolor('white')
plt.axis('off')  # enlève axes, graduations, cadre

# Affichage
plt.show()

# pas mal :
#2ca02c # vert
#c0392b #rouge
#6fa8dc # bleu pastel
#1abc9c #turquoise
