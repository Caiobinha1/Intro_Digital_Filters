import numpy as np
import struct
import os

# Define fixed directories, ensure the terminal is in the correct folder
INPUT_DIR = "input"
OUTPUT_DIR = "output"

# Function to load coefficients based on the selected filter type
def load_coefficients():
    options = {
        1: "low_pass_coefficients.txt",
        2: "high_pass_coefficients.txt",
        3: "band_pass_coefficients.txt",
        4: "band_stop_coefficients.txt"
    }

    print("Select the type of filter to apply:")
    print("1 - Low Pass")
    print("2 - High Pass")
    print("3 - Band Pass")
    print("4 - Band Stop")

    choice = int(input("Enter the number of your choice: "))

    if choice not in options:
        raise ValueError("Invalid choice! Please select a number between 1 and 4.")

    coef_file = options[choice]
    coef_path = os.path.join(INPUT_DIR, coef_file)

    if not os.path.exists(coef_path):
        raise FileNotFoundError(f"Coefficient file '{coef_file}' not found in '{INPUT_DIR}'.")

    with open(coef_path, "r") as f:
        coefficients = [float(line.strip()) for line in f]

    return np.array(coefficients)

# Function to apply the coefficients to a .pcm file
def apply_filter(input_file, output_file, coefficients, bits):
    # Determine data format based on bit depth
    fmt = "h" if bits == 16 else "i"
    sample_size = 2 if bits == 16 else 4

    input_path = os.path.join(INPUT_DIR, input_file)
    output_path = os.path.join(OUTPUT_DIR, output_file)

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file '{input_file}' not found in '{INPUT_DIR}'.")

    with open(input_path, "rb") as input_audio:
        audio_data = input_audio.read()

    # Convert bytes to a sample array
    samples = np.array(struct.unpack(f"{len(audio_data)//sample_size}{fmt}", audio_data))

    # Apply the filter using convolution
    filtered_samples = np.convolve(samples, coefficients, mode="same").astype(np.int32)

    # Clip values to avoid overflow when saving
    max_value = 2**(bits - 1) - 1
    min_value = -2**(bits - 1)
    filtered_samples = np.clip(filtered_samples, min_value, max_value).astype(fmt)

    # Convert filtered array back to bytes
    filtered_audio = struct.pack(f"{len(filtered_samples)}{fmt}", *filtered_samples)

    # Save the filtered audio
    with open(output_path, "wb") as output_audio:
        output_audio.write(filtered_audio)

    print(f"Filtered file saved to: {output_path}")

# Main program
if __name__ == "__main__":
    # Load coefficients
    coefficients = load_coefficients()

    # Request parameters from the user
    input_file = input("Enter the name of the audio file (.pcm) to be processed (e.g., input.pcm): ")
    output_file = input("Enter the name of the output file (.pcm) (e.g., output.pcm): ")
    bits = int(input("Enter the bit depth (16 or 32): "))

    if bits not in [16, 32]:
        raise ValueError("Invalid bit depth! Choose 16 or 32.")

    apply_filter(input_file, output_file, coefficients, bits)
