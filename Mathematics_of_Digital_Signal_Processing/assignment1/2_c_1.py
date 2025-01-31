# Letong Zhou / 2210365 / Mathematics / 3rd year

import numpy as np
import matplotlib.pyplot as plt

def sum_sequences(x, y):
    """
    inputs:
    x (numpy.ndarray): Sequence x[n]
    y (numpy.ndarray): Sequence y[n]

    Returns:
    Sequence z[n] = x[n] + y[n]
    """
    return x + y


# Define parameters
A = B = 1  # Amplitudes
f0 = 1  # Frequency of x[n]
f1 = 2  # Frequency of y[n]
phi1 = 0  # Phase shift of x[n]
phi2 = np.pi / 2  # Phase shift of y[n]
N = 100  # Number of samples

# Generate n values
n = np.arange(N)

# Generate sequences x[n] and y[n]
x_n = A * np.sin(2 * np.pi * f0 * n + phi1)
y_n = B * np.cos(2 * np.pi * f1 * n + phi2)

# Compute the sum z[n] = x[n] + y[n]
z_n = sum_sequences(x_n, y_n)

# Plot x[n], y[n], and z[n]
plt.figure(figsize=(12, 8))

# Plot x[n]
plt.subplot(3, 1, 1)
plt.plot(n, x_n, label='x[n] = sin(2πf0n + ϕ1)')
plt.title('Signal x[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Plot y[n]
plt.subplot(3, 1, 2)
plt.plot(n, y_n, label='y[n] = cos(2πf1n + ϕ2)', color='orange')
plt.title('Signal y[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Plot z[n]
plt.subplot(3, 1, 3)
plt.plot(n, z_n, label='z[n] = x[n] + y[n]', color='green')
plt.title('Sum of Signals z[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Adjust layout and show plot
plt.tight_layout()
plt.show()