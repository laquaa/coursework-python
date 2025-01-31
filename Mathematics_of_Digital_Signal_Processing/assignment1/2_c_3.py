# Letong Zhou / 2210365 / Mathematics / 3rd year

import numpy as np

# The mathematical expression is on the written part

def calculate_energy(N):
    # Define the frequency and phase shift within the function
    f0 = 1  # frequency of the sine function
    phi1 = 0  # phase shift of the sine function

    # Generate the sequence x[n] = sin(2*pi*f0*n + phi1)
    # Here, since f0=1 and phi1=0, x[n] simplifies to sin(2*pi*n)
    n = np.arange(N)
    x = np.sin(2 * np.pi * f0 * n + phi1)

    # Calculate the energy of the sequence, which is the sum of the squares of the elements
    energy = np.sum(x ** 2)

    return energy

# Example
N = 10
computed_energy = calculate_energy(N)

# The theoretical energy, known to be 0 due to the nature of sin(2*pi*n)
theoretical_energy = 0

print("Computed Energy:", computed_energy)
print("Theoretical Energy:", theoretical_energy)

