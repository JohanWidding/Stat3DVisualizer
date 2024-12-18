import numpy as np

class RandomDataGenerator:
    def generate_data(self, n_points=100):
        x = np.random.uniform(-10, 10, n_points)
        y = np.random.uniform(-10, 10, n_points)
        noise = np.random.normal(0, 1, n_points)
        z = 2 * x + 3 * y + noise
        return x, y, z
