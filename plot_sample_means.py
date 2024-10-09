import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_sample_means(scale, n_samples, sample_size):
    """
    Plots the distribution of sample means from an exponential distribution.

    Args:
        scale (float): The scale parameter of the exponential distribution.
        n_samples (int): The number of samples to draw.
        sample_size (int): The size of each sample.
    """

    data = np.random.exponential(scale=scale, size=n_samples * sample_size)
    means = [np.mean(data[i * sample_size:(i + 1) * sample_size]) for i in range(n_samples)]

    mean = np.mean(means)
    std = np.std(means)

    plt.figure(figsize=(10, 6))

    plt.hist(means, bins=50, density=True, alpha=0.6, color=(0.1, 0.2, 0.8), edgecolor='black')

    xfit = np.linspace(min(means), max(means), 100)
    yfit = norm.pdf(xfit, mean, std)

    plt.plot(xfit, yfit, 'r-', lw=2, label=f"Normal fit (μ={mean:.2f}, σ={std:.2f})")

    plt.title('Distribution of Sample Means', fontsize=14)
    plt.xlabel('Sample Mean', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.grid(True)
    plt.legend()

    plt.show()
