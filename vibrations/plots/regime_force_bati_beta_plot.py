import numpy as np
import matplotlib.pyplot as plt

# =========================
# Paramètres du système
# =========================
m = 7
k = 100
c = 10

# ζ choisi par l'utilisateur
zeta = 0.7

# =========================
# Axe fréquentiel : r = ω/ω0
# =========================
r = np.linspace(0, 5, 2000)

# Courbe conservatif (ζ = 0)
beta_conservatif = (r**2) / np.sqrt((1 - r**2)**2)

# Courbe utilisateur
beta_user = (r**2) / np.sqrt((1 - r**2)**2 + (2 * zeta * r)**2)

# =========================
# Liste des ζ_p demandés
# 0 -> 0.3 pas 0.05, puis 0.3 -> 0.8 pas 0.1
# =========================
zetas_1 = np.arange(0.05, 0.30 + 1e-12, 0.05)
zetas_2 = np.arange(0.30, 0.80 + 1e-12, 0.10)
zeta_p_list = np.unique(np.concatenate([zetas_1, zetas_2]))

# =========================
# Plot
# =========================
plt.figure()

# Courbe conservatif (ζ=0) en pointillés
plt.semilogy(r, beta_conservatif, linestyle="--", linewidth=1.5, alpha=0.8, label=r"Conservatif ($\zeta=0$)")

# Famille de courbes (ζ_p)
for zeta_p in zeta_p_list:
    beta_p = 1 / np.sqrt((1 - r**2)**2 + (2 * zeta_p * r)**2)
    plt.semilogy(r, beta_p, linewidth=1, alpha=0.5, label=fr"$\zeta={zeta_p:.2f}$")

# Courbe utilisateur mise en évidence
plt.semilogy(r, beta_user, linewidth=2.5, color="#f59e0b", label=fr"$\zeta (utilisateur)={zeta:.2f}$")



plt.xlabel(r"$\omega / \omega_0$")
plt.ylabel(r"$|\beta|$")
plt.title("Étude fréquentielle — module de β")
plt.grid(True, which="both")
plt.legend(ncol=2, fontsize=9)
plt.ylim(1e-2, 1e2)  # optionnel : évite des valeurs trop extrêmes
plt.show()
