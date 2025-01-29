#EMA - Exponencial mean avarage - Media Movel Exponencial
import numpy as np
import pylab

# Read the PCM file
Sound_data = np.memmap("input/voice_noise.pcm", dtype='h', mode='r')

# Create a new array for the filtered data
New_data = np.memmap("output/resultEMA.pcm", dtype='h', mode='w+', shape=Sound_data.shape)

# Moving average value -- affects the smoothing factor
k = int(input("Enter the smoothing factor (higher = more smoothing): "))

# Compute the smoothing factor alpha for EMA
alpha = 2 / (k + 1)

# Initialize the first value (EMA_0 = first sample)
New_data[0] = Sound_data[0]

# Apply the Exponential Moving Average formula
for t in range(1, len(Sound_data)):
    New_data[t] = alpha * Sound_data[t] + (1 - alpha) * New_data[t - 1]

# Visualize the result
pylab.plot(New_data)
pylab.title("New Wave with Exponential Moving Average (EMA) Filter")
pylab.xlabel("Time (s.10^4)")
pylab.ylabel("Amplitude")
pylab.show()
