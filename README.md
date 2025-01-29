# IIR and FIR Filters

This repository contains implementations of both **Finite Impulse Response (FIR)** and **Infinite Impulse Response (IIR)** filters, commonly used in digital signal processing. The repository is divided into two main folders:

- **`FIR/`**: Contains implementations of FIR filters, including the Simple Moving Average (SMA) and Exponential Moving Average (EMA).
- **`IIR/`**: Contains implementations of IIR filters, such as the Least Mean Squares (LMS) adaptive filter.

## Getting Started

### Prerequisites
To run the filter implementations, ensure you have the following installed:
- Python 3.x
- NumPy
- Matplotlib (for visualization)

### Folder Structure
```
.
├── FIR/
│   ├── SMA.py
│   ├── EMA.py
│   ├── README.md
|   ├── input/  # Folder for input PCM audio files
|   ├── output/ # Folder for processed output PCM files
├── IIR/
│   ├── LMS.py
│   ├── README.md
|   ├──
|   ├── output
├── README.md (this file)
```

## Running the Filters
Each filter script processes PCM audio data from the `input/` folder and saves the filtered output in `output/`. Check the individual `README.md` files inside the `FIR/` and `IIR/` folders for details on how to run and modify the scripts.

## Customization
You can tweak the filter parameters in the scripts:
- **SMA & EMA**: Modify the window size `k`.
- **LMS Filter**: Adjust the number of coefficients (`n_coef`) and step size (`passo`) for convergence speed and accuracy.

---
For further explanations on digital filters, refer to the individual `README.md` files in the respective folders.

