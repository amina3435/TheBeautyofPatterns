Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

G = 6.67430e-11  # gravitational constant
M_sun = 1.989e30  # mass of the Sun

# Mass of planets (in kg)
M_earth = 5.972e24
M_mars = 6.39e23

# Average distance to the Sun (in m)
r_earth = 1.496e11
r_mars = 2.279e11

# Initial conditions [x, y, vx, vy] for Earth and Mars
Y0_earth = [r_earth, 0, 0, np.sqrt(G*M_sun/r_earth)]
Y0_mars = [r_mars, 0, 0, np.sqrt(G*M_sun/r_mars)]
Y0 = Y0_earth + Y0_mars

def dydt(Y, t):
    # Unpack the state vector Y
    x_earth, y_earth, vx_earth, vy_earth, x_mars, y_mars, vx_mars, vy_mars = Y

    # Compute the distances
    r_earth = np.sqrt(x_earth**2 + y_earth**2)
    r_mars = np.sqrt(x_mars**2 + y_mars**2)

    # Compute the accelerations
    ax_earth = -G * M_sun / r_earth**3 * x_earth
    ay_earth = -G * M_sun / r_earth**3 * y_earth
    ax_mars = -G * M_sun / r_mars**3 * x_mars
    ay_mars = -G * M_sun / r_mars**3 * y_mars

    return [vx_earth, vy_earth, ax_earth, ay_earth, vx_mars, vy_mars, ax_mars, ay_mars]

# Time array
T = np.linspace(0, 1e8, 1000)  # 1000 points over 1e8 seconds

# Solve the ODE
Y = odeint(dydt, Y0, T)

# Plot the orbits
plt.figure(figsize=(10,10))
plt.plot(Y[:,0], Y[:,1], label='Earth')
plt.plot(Y[:,4], Y[:,5], label='Mars')
plt.legend()
plt.show()