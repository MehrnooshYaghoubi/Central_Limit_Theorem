# Central Limit Theorem

Our goal here is to demonstrate the Central Limit Theorem. To do this, we simulate random samples from an exponential distribution, calculate their means, and visualize the distribution of these means. According to the Central Limit Theorem, regardless of the type of the original distribution, when the sample size is sufficiently large, the distribution of sample means approaches a normal distribution, even if the initial distribution is not normal.

1. **Probability Density Function (PDF):**
   
  $$f(x; \theta) 0 \leq \lambda e^{\lambda x-}\space\space\text{for}\space\space x=f(x;\lambda)$$

3. **Mean:**
   - The mean of the exponential distribution is expressed as:
  $$\text{Mean} = \mu =
  \frac{1}{\lambda}$$

4. **Standard Deviation:**
   - The standard deviation of the exponential distribution is also given by:

$$\sigma=\frac{1}{\lambda}$$


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
