import numpy as np
import matplotlib.pyplot as plt

def generate_beetle_suture(a, b, kappa, points=200):
    """
    Génère les coordonnées d'un lobe ellipsoïdal optimisé.
    a: demi-grand axe
    b: demi-petit axe
    kappa: coefficient d'imbrication
    """
    theta = np.linspace(0, 2*np.pi, points)
    
    # Équations paramétriques inspirées du Phloeodes diabolicus
    x = a * np.cos(theta)
    y = b * np.sin(theta) * (1 + kappa * np.cos(theta))
    
    return x, y

# Paramètres optimaux identifiés dans le Manifeste
a_param = 1.2  # Ratio ellipsoïdal
b_param = 0.8
kappa_interlock = 0.25 # Angle de contact ~25°

x_coords, y_coords = generate_beetle_suture(a_param, b_param, kappa_interlock)

plt.figure(figsize=(8, 4))
plt.plot(x_coords, y_coords, label='Interface Ellipsoïdale Optimisée', color='indigo', lw=2)
plt.fill_between(x_coords, y_coords, alpha=0.2, color='indigo')
plt.title("Géométrie de Suture - Protocole Ouellette")
plt.xlabel("Axe de contrainte latérale (x)")
plt.ylabel("Profondeur d'imbrication (y)")
plt.grid(True, linestyle='--')
plt.axis('equal')
plt.legend()
plt.show()
