import numpy as np
def generate_data(total_points, smoothness_factor, num_extremes):
    x = np.linspace(0, 1, total_points)
    frequency = num_extremes
    y = np.sin(frequency * np.pi * x)
    noise_level = 1 / smoothness_factor
    noise = np.random.normal(0, noise_level, total_points)
    y += noise
    return x, y
