# Central Limit Theorem Demonstration

**Objective**

This demonstration aims to illustrate the Central Limit Theorem (CLT) by simulating random samples from an exponential distribution, calculating their means, and visualizing the resulting distribution. The CLT asserts that, regardless of the underlying distribution, the distribution of sample means approaches a normal distribution as the sample size increases.


## **Exponential Distribution**

**Probability Density Function (PDF):**

$$f(x; \theta)= \frac{1}{\theta} e^{-\frac{x}{\theta}} \quad \text{for} \quad x \geq 0$$

**Mean:**
  $$\mu = \theta$$

**Standard Deviation:**
  $$\sigma = \theta$$

**Features**

- Generates random samples from an exponential distribution.
- Plots the distribution of sample means.
- Fits a normal distribution to the sample means.

**Requirements**

- Python 3.x
- Libraries: `numpy`, `matplotlib`, `scipy`

**Installation**

To install the necessary dependencies, execute the following command:

```bash
pip install -r requirements.txt
