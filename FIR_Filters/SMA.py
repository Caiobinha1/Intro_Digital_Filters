#SMA - Simple Moving Average (SMA) - Media Movel Simples
import numpy as np
import pylab

# Read the PCM file
Sound_data = np.memmap("input/voice_noise.pcm", dtype='h', mode='r')

# Create a new array for the filtered data
New_data = np.memmap("output/resultMA.pcm", dtype='h', mode='w+', shape=Sound_data.shape)

# Moving average value -- average of the previous k values
k = int(input("Enter the moving average value: "))

# Calculate the moving average using cumulative sum
cumulative_sum = np.cumsum(Sound_data, dtype=float)
New_data[:k] = cumulative_sum[:k] / (np.arange(k) + 1)  # Handle the first values (partial windows)
New_data[k:] = (cumulative_sum[k:] - cumulative_sum[:-k]) / k  # Average of the complete windows

# Visualize the result
pylab.plot(New_data)
pylab.title(f"New Wave with Moving Average Filter")
pylab.xlabel("Time (s.10^4)")
pylab.ylabel("Amplitude")
pylab.show()
