import librosa
import numpy as np
import scipy.signal
import os

def extract_loudest_partials(audio_path, num_partials=15):
    # Load the audio file as mono
    y, sr = librosa.load(audio_path, sr=None, mono=True)

    # Compute the FFT
    fft = np.fft.rfft(y)
    freqs = np.fft.rfftfreq(len(y), 1/sr)

    # Convert magnitude to dB
    magnitude = np.abs(fft)
    db = 20 * np.log10(magnitude + 1e-10)  # Avoid log(0)

    # Find peaks in the spectrum
    peaks, _ = scipy.signal.find_peaks(db, distance=20)

    # Get the loudest peaks
    loudest_indices = peaks[np.argsort(db[peaks])][-num_partials:]

    # Sort them by frequency
    loudest_indices = loudest_indices[np.argsort(freqs[loudest_indices])]

    # Create output filename
    base = os.path.splitext(os.path.basename(audio_path))[0]
    output_path = f"{base}_partials.txt"

    # Write to file
    with open(output_path, "w") as f:
        f.write("Frequency (Hz)\tDecibel (dB)\n")
        for idx in loudest_indices:
            f.write(f"{freqs[idx]:.2f}\t{db[idx]:.2f}\n")

    print(f"Top {num_partials} partials saved to {output_path}")

# Example usage
if __name__ == "__main__":
    input_file = "466519__tarane468__001-kankles-c3.wav"  # Replace with your audio file path
    extract_loudest_partials(input_file)
