# This code generates the coefficients required for simple filters
import numpy as np
import pylab

def hamming_window(i, value):
    return 0.54 - 0.46 * np.cos(2 * np.pi * i / (value - 1))

def sinc_function(fc, i, value):
    if (i - (value - 1) / 2) == 0:
        return 2 * np.pi * fc
    else:
        return (np.sin(2 * np.pi * fc * (i - (value - 1) / 2))) / (i - (value - 1) / 2)

def normalize(data, total):
    return [x / total for x in data]

def write_to_file(filename, data):
    with open(filename, "w") as coefficients:
        for i in data:
            coefficients.write("{:.12f}\n".format(i))

def plot_data(data):
    pylab.plot(data)
    pylab.show()

def band_pass_filter(value, FC, FC2):
    high_data = []
    low_data = []
    band = []
    sum_high = 0
    sum_low = 0

    for i in range(value):
        high_data.append(sinc_function(FC, i, value) * hamming_window(i, value))
        low_data.append(sinc_function(FC2, i, value) * hamming_window(i, value))
        sum_high += high_data[i]
        sum_low += low_data[i]

    high_data = normalize(high_data, sum_high)
    low_data = normalize(low_data, sum_low)

    for i in range(value):
        high_data[i] = -high_data[i]
    high_data[int(value / 2)] += 1

    for i in range(value):
        band.append(-1 * (high_data[i] + low_data[i]))
    band[int(value / 2)] += 1

    write_to_file("input\\band_pass_coefficients.txt", band)
    plot_data(band)
    return band

def band_stop_filter(value, FC, FC2):
    high_data = []
    low_data = []
    band = []
    sum_high = 0
    sum_low = 0

    for i in range(value):
        high_data.append(sinc_function(FC, i, value) * hamming_window(i, value))
        low_data.append(sinc_function(FC2, i, value) * hamming_window(i, value))
        sum_high += high_data[i]
        sum_low += low_data[i]

    high_data = normalize(high_data, sum_high)
    low_data = normalize(low_data, sum_low)

    for i in range(value):
        high_data[i] = -high_data[i]
    high_data[int(value / 2)] += 1

    for i in range(value):
        band.append(high_data[i] + low_data[i])

    write_to_file("input\\band_stop_coefficients.txt", band)
    plot_data(band)

def low_pass_filter(value, FC):
    low_data = []
    sum_low = 0

    for i in range(value):
        low_data.append(sinc_function(FC, i, value) * hamming_window(i, value))
        sum_low += low_data[i]

    low_data = normalize(low_data, sum_low)

    write_to_file("input\\low_pass_coefficients.txt", low_data)
    plot_data(low_data)
    return low_data

def high_pass_filter(value, FC):
    high_data = []
    sum_high = 0

    for i in range(value):
        high_data.append(sinc_function(FC, i, value) * hamming_window(i, value))
        sum_high += high_data[i]

    high_data = normalize(high_data, sum_high)

    for i in range(value):
        high_data[i] = -high_data[i]
    high_data[int(value / 2)] += 1

    write_to_file("input\\high_pass_coefficients.txt", high_data)
    plot_data(high_data)
    return high_data

def main():
    choice = int(input("1-Low Pass\n2-High Pass\n3-Band Pass\n4-Band Stop\n"))
    value = int(input("Enter the number of coefficients: "))
    FS = int(input("Enter the audio frequency: "))

    if value % 2 == 0:
        print("The chosen value is even, so the precision will not be very high.")

    cutoff_freq = int(input("Enter the desired low cutoff frequency: "))
    FC = cutoff_freq / FS

    if choice in [3, 4]:
        cutoff_freq2 = int(input("Enter the desired high cutoff frequency: "))
        FC2 = cutoff_freq2 / FS

    actions = {
        1: lambda: low_pass_filter(value, FC),
        2: lambda: high_pass_filter(value, FC),
        3: lambda: band_pass_filter(value, FC, FC2),
        4: lambda: band_stop_filter(value, FC, FC2)
    }

    if choice in actions:
        if choice == 4 and cutoff_freq2 > cutoff_freq:
            print("Error: Low cutoff frequency is lower than high cutoff frequency!")
        else:
            actions[choice]()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
