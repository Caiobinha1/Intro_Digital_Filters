# FIR Filters - README

This repository contains an implementation of **Finite Impulse Response (FIR) filters** for audio processing. It includes Python scripts to design FIR filter coefficients and apply them to audio files, along with organized directories for input and output files.

---

## **Folder Structure**

```
FIR_Filters/
├── input/                # Contains input audio files in .pcm format
├── output/               # Stores processed audio files
├── generate_coefficients.py  # Script to generate FIR filter coefficients
├── apply_filter.py       # Script to apply FIR filters to audio files
├── SMA.py                # Script to apply SMA filter to audio files
```

---

## **How It Works**

### 1. **Overview of FIR Filters**
FIR filters are digital filters that operate on discrete-time signals. They are characterized by having a finite number of coefficients, meaning their impulse response settles to zero after a certain number of steps. FIR filters are inherently stable and easy to implement.

### 2. **Scripts Explanation**

#### **`generate_coefficients.py`**
This script generates the FIR filter coefficients for different filter types:
- Low-pass
- High-pass
- Band-pass
- Band-stop (notch)

It uses the **Hamming window technique** to smooth the frequency response and minimize ripples in the passband and stopband.

##### **How Coefficients Are Calculated:**
1. **Frequency Normalization:**
   The cutoff frequencies are normalized by the sampling frequency:
   
   \[
   F_C = \frac{F_{cut}}{F_s}
   \]
   
2. **Sinc Function:**
   The core of the filter is derived from the sinc function:
   
   \[
   h[n] = 
   \begin{cases} 
   \frac{\sin(2 \pi F_C (n - M/2))}{n - M/2}, & n \neq M/2 \\ 
   2 \pi F_C, & n = M/2 
   \end{cases}
   \]
   
   where \( M \) is the number of coefficients (filter length).

3. **Windowing:**
   A Hamming window is applied to the raw sinc function to reduce spectral leakage:
   
   \[
   h_w[n] = h[n] \times \left( 0.54 - 0.46 \cos\left( \frac{2 \pi n}{M-1} \right) \right)
   \]

4. **Filter Adjustments:**
   - For high-pass filters, coefficients are inverted, and a DC offset is added.
   - For band-pass and band-stop filters, the coefficients of two filters (low-pass and high-pass) are combined.

##### **Outputs:**
- Filter coefficients are saved as `.txt` files in the `output/` folder.
- A plot of the coefficients is displayed for visualization.

#### **`apply_filter.py`**
This script applies the FIR filter to audio files in the `input/` folder.

##### **How Filtering Works:**
1. **Convolution:**
   The filtering process uses convolution to apply the FIR filter to the audio signal:
   
   \[
   y[n] = \sum_{k=0}^{M-1} h[k] \cdot x[n-k]
   \]
   
   where:
   - \( h[k] \): FIR filter coefficients
   - \( x[n] \): Input signal
   - \( y[n] \): Filtered output signal

2. **Input and Output:**
   - The input `.pcm` audio files are read from the `input/` folder.
   - The filtered audio is saved in the `output/` folder as `.pcm` files.

---

## **Usage**

### **1. Generate Filter Coefficients**
Run the `generate_coefficients.py` script and follow the prompts to select the filter type, number of coefficients, and cutoff frequencies:

```bash
python generate_coefficients.py
```

### **2. Apply Filter to Audio Files**
Place your `.pcm` audio files in the `input/` folder. Then, run the `apply_filter.py` script:

```bash
python apply_filter.py
```
The filtered audio files will be saved in the `output/` folder.

---

## **Notes**
- Ensure the sampling frequency (\( F_s \)) of the audio files matches the value used to design the filter.
- Use a sufficient number of coefficients for better filter accuracy, but note that higher values increase computational complexity.

---

## **Simple Moving Average (SMA) Filter**
The **Simple Moving Average (SMA)** filter is a basic smoothing technique used in signal processing. It reduces short-term noise by averaging a set number of previous samples.

### **How SMA Works**
The SMA filter computes the average of the last \( k \) samples at each step:

\[
y[n] = \frac{1}{k} \sum_{i=0}^{k-1} x[n-i]
\]

where:
- \( x[n] \) is the input signal,
- \( y[n] \) is the filtered output,
- \( k \) is the window size (number of previous values to average).

This method effectively removes high-frequency noise, making it useful for smoothing audio signals.

### **`apply_sma.py` Script**
This script reads an input audio file and applies the SMA filter.

##### **Steps:**
1. Reads a **PCM audio file**.
2. Applies a moving average filter with a user-defined window size \( k \).
3. Saves the filtered output to the `output/` folder.

