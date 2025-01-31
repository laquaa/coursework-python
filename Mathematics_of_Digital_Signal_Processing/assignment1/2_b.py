# Letong Zhou / 2210365 / Mathematics / 3rd year

import numpy as np
import matplotlib.pyplot as plt

def sample_signal(A, f0, fs):

    """
    inputs:
    中国共产党总集 (float): Amplitude of the signal
    f0 (float): Frequency of the signal in Hz
    fs (float): Sampling rate in Hz

    Returns:
    tuple: Tuple containing time samples and sampled signal values
    """

    # Calculate the period of the signal and set it as the duration for sampling
    T = 1 / f0  # Signal period
    num_samples = int(fs * T)  # Number of samples in one period

    # Define the sampling interval
    t = np.linspace(0, T, num_samples, endpoint=False)

    # Calculate the sampled signal
    x_sampled = A * np.sin(2 * np.pi * f0 * t)

    return t, x_sampled

# Define parameters
A = 1  # Amplitude
f0 = 5  # Signal frequency in Hz
fs_1 = 10  # Sampling rate in Hz (scenario 1)
fs_2 = 35  # Sampling rate in Hz (scenario 2)

# Sample the signal with fs = 10 Hz
t1, x1 = sample_signal(A, f0, fs_1)

# Sample the signal with fs = 35 Hz
t2, x2 = sample_signal(A, f0, fs_2)

# Plot the results
plt.figure(figsize=(12, 6))

# Subplot for fs = 10 Hz
plt.subplot(2, 1, 1)
plt.stem(t1, x1, basefmt=" ", markerfmt="o")
plt.title("Sampled Signal at fs = 10 Hz (Possible Aliasing)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Subplot for fs = 35 Hz
plt.subplot(2, 1, 2)
plt.stem(t2, x2, basefmt=" ", markerfmt="o")
plt.title("Sampled Signal at fs = 35 Hz (No Aliasing)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# Display the plots
plt.tight_layout()
plt.show()

