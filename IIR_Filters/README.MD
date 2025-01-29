# IIR Filters: Exponential Moving Average (EMA) and Least Mean Squares (LMS)

This repository contains implementations of two Infinite Impulse Response (IIR) filters:
- **Exponential Moving Average (EMA)**: A low-pass filter used for smoothing signals.
- **Least Mean Squares (LMS) Adaptive Filter**: A self-adjusting filter commonly used for noise cancellation.

## 📂 Folder Structure
```
IIR_Filters/
│-- EMA_Filter.py      # Exponential Moving Average filter implementation
│-- LMS_Filter.py      # Least Mean Squares filter implementation
│-- input/             # Folder for input PCM audio files
│-- output/            # Folder for filtered output PCM files
│-- README.md          # Documentation
```

---

## 📌 Exponential Moving Average (EMA)
### 🔹 **Mathematical Formula**
The EMA filter is defined as:

\[ y[n] = \alpha \cdot x[n] + (1 - \alpha) \cdot y[n-1] \]

Where:
- \( y[n] \) is the filtered signal at time \( n \)
- \( x[n] \) is the input signal at time \( n \)
- \( \alpha \) is the smoothing factor (0 < \( \alpha \) < 1), which controls how much the filter reacts to changes.

### 🔹 **How to Run EMA Filter**
1. Place your input PCM file inside the `input/` folder.
2. Run the script:
   ```sh
   python EMA_Filter.py
   ```
3. The filtered output will be saved as `output/filtered_ema.pcm`.
4. You can adjust `alpha` to change the smoothing effect.

---

## 📌 Least Mean Squares (LMS) Adaptive Filter
### 🔹 **Mathematical Formula**
The LMS filter updates its coefficients using the following rule:

\[ e[n] = d[n] - \sum_{k=0}^{N-1} w_k \cdot x[n-k] \]
\[ w_k = w_k + \mu \cdot e[n] \cdot x[n-k] \]

Where:
- \( e[n] \) is the error signal (difference between desired and estimated output).
- \( d[n] \) is the desired (clean) signal.
- \( x[n] \) is the input (noisy) signal.
- \( w_k \) are the adaptive filter coefficients.
- \( \mu \) is the step size, controlling convergence speed and accuracy.

### 🔹 **How to Run LMS Filter**
1. Place `far.pcm` (noisy audio) and `near.pcm` (clean reference audio) inside the `input/` folder.
2. Run the script:
   ```sh
   python LMS_Filter.py
   ```
3. The filtered output will be saved as `output/lms_output.pcm`.
4. You can adjust `n_coef` (filter size) and `step_size` to optimize performance.

---

## 🔧 **Modifying Parameters**
- **For EMA:** Change `alpha` (0.01 to 0.5 for different smoothing levels).
- **For LMS:** Adjust `n_coef` (filter order) and `step_size` (convergence rate).

---

## 🎯 **Conclusion**
- **EMA** is useful for smoothing signals with a predefined smoothing factor.
- **LMS** is an adaptive filter that dynamically adjusts its coefficients to minimize error, useful for real-time noise cancellation.

Both filters can be fine-tuned by modifying their parameters for optimal results!

---

💡 **Need help?** Feel free to reach out! 🚀

