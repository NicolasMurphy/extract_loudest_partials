# Extract Loudest Partials

A simple script to extract the 15 loudest partials from an audio file, inspired by Deru.

## Usage

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Add an audio file (e.g., `.wav`, `.mp3`) to the **root of the repository**.

    > The audio file should be **short** and feature an **instrument playing a single note** for best results.

3. Open `extract_loudest_partials.py` and update this line with the name of your audio file:

    ```python
    input_file = "your-audio-file.wav"  # Replace with your audio file path
    ```

4. Run the script:

    ```bash
    python extract_loudest_partials.py
    ```

    This will generate a file named `your-audio-file_partials.txt`, containing the 15 strongest frequency peaks (in Hz and dB).

## Notes

- Works with mono or stereo audio (stereo is automatically averaged to mono).
- Supports common audio formats via `librosa`.
