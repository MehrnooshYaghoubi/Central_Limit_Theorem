# Central Limit Theorem

Our goal here is to demonstrate the Central Limit Theorem. To do this, we simulate random samples from an exponential distribution, calculate their means, and visualize the distribution of these means. According to the Central Limit Theorem, regardless of the type of the original distribution, when the sample size is sufficiently large, the distribution of sample means approaches a normal distribution, even if the initial distribution is not normal.

1. **Probability Density Function (PDF):**
   \[
   &&f(x; \theta) = \frac{1}{\theta} e^{-\frac{x}{\theta}} \quad \text{for} \quad x \geq 0&&
   \]

2. **Mean:**
   - The mean of the exponential distribution is expressed as:
   \[
   &&\text{Mean} = \mu = \theta&&
   \]

3. **Standard Deviation:**
   - The standard deviation of the exponential distribution is also given by:
   \[
   &&\sigma = \theta&&
   \]

The exponential distribution has a parameter called &&\( \theta \)&& (scale), which represents the mean time between events. In this context, &&\( \theta \)&& is the inverse of the rate &&\( \lambda \)&&, where &&\( \lambda = \frac{1}{\theta} \)&&.


## Features
- Generates random samples from an exponential distribution.
- Plots the distribution of sample means.
- Fits a normal distribution to the sample means.

## Requirements
- Python 3.x
- Libraries: `numpy`, `matplotlib`, `scipy`

## Installation
To install the required dependencies, run:
```bash
pip install -r requirements.txt
