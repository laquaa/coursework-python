# Letong Zhou / 2210365 / Mathematics / 3rd year

import numpy as np
import matplotlib.pyplot as plt

def time_reverse_and_scale(x):
    """
    inputs:
    x (numpy.ndarray): Sequence x[n]

    Returns:
    Sequence w[n] = αx[-n], where α is the scaling factor (0.5)
    """
    alpha = 0.5  # Scaling factor
    x_reversed = x[::-1]  # Time-reversed sequence
    w = alpha * x_reversed  # Scaled time-reversed sequence
    return w


# Define parameters
A = 1  # Amplitude of x[n]
f0 = 1  # Frequency of x[n]
phi1 = 0  # Phase shift of x[n]
N = 100  # Number of samples

# Generate n values for x[n]
n = np.arange(N)

# Generate sequence x[n]
x_n = A * np.sin(2 * np.pi * f0 * n + phi1)

# Compute w[n] = αx[-n]
w_n = time_reverse_and_scale(x_n)

# Generate n values for plotting from -N+1 to 0
n_reversed = np.arange(-N + 1, 1)

# Plot x[n] and w[n]
plt.figure(figsize=(10, 6))

# Plot x[n] (original sequence)
plt.subplot(2, 1, 1)
plt.plot(n, x_n, label='x[n] = sin(2πf0n + ϕ1)')
plt.title('Original Signal x[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Plot w[n] (time-reversed and scaled sequence)
plt.subplot(2, 1, 2)
plt.plot(n_reversed, w_n, label='w[n] = 0.5 * x[-n]', color='red')
plt.title('Time-Reversed and Scaled Signal w[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Adjust layout and show plot
plt.tight_layout()
plt.show()