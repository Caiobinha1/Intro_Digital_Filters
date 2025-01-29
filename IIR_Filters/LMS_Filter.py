import numpy as np
import pylab 

# Define parameters
n_coef = 71  # Minimum value of n_coef that still provides a desirable result
step_size = 1e-11  # Step size affects error convergence speed and accuracy

# Initialize arrays
x_samples = np.zeros(n_coef, dtype=float)
coefficients = np.zeros(n_coef, dtype=float)

# Load input audio data
x_data = np.memmap("input/far_apcm.pcm", dtype='h', mode='r')  # Must be white noise
d = np.memmap("input/near_apcm.pcm", dtype='h', mode='r')

# Create output file
filtered_data = np.memmap("output/saidaadp.pcm", dtype='h', mode='w+', shape=x_data.shape)

errors = []

# Adaptive filtering process
for i in range(x_data.size):
    x_samples[0] = x_data[i]
    
    y = 0
    for s in range(n_coef):
        y += x_samples[s] * coefficients[s]
    
    error = d[i] - y
    errors.append(error)
    
    for s in range(n_coef):
        coefficients[s] += step_size * float(error) * x_samples[s]
    
    # Shift sample buffer
    x = n_coef
    while x > 0:
        x -= 1
        x_samples[x] = x_samples[x - 1]

# Store filtered output
for i in range(x_data.size):
    filtered_data[i] = errors[i]

# Plot error evolution
pylab.plot(errors)
pylab.title("Error Convergence")
pylab.show()

# Plot filter coefficients
pylab.plot(coefficients)
pylab.title("Filter Coefficients")
pylab.show()
