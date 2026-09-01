import os
import numpy as np
import scipy.signal as signal
from scipy.io import wavfile
import matplotlib.pyplot as plt

# 1. Load Audio File
sample_rate, audio_data = 22050, None
audio_path = os.path.join(os.path.dirname(__file__), "..", "dataSet", "AudioFile.mp3")
output_path = os.path.join(os.path.dirname(__file__), "cloned_audio.wav")

# For lab demo: Generate / Read audio signal
duration = 3  # seconds
t = np.linspace(0, duration, int(sample_rate * duration))

# Original Voice Signal (Fundamental pitch ~ 150 Hz + harmonics)
original_voice = (
    0.6 * np.sin(2 * np.pi * 150 * t) +
    0.3 * np.sin(2 * np.pi * 300 * t) +
    0.1 * np.sin(2 * np.pi * 450 * t)
)

# 2. Audio / Voice Cloning Transformation (Pitch & Timbre Shift)
# Target Speaker Voice: Shift pitch factor (e.g., to 220 Hz target voice)
pitch_factor = 1.4  # > 1.0 increases pitch (higher voice), < 1.0 lowers pitch
cloned_voice = signal.resample(original_voice, int(len(original_voice) / pitch_factor))
cloned_voice = signal.resample(cloned_voice, len(original_voice))  # restore duration

# Add formant/timbre filter
b, a = signal.butter(4, 0.3, btype='low')
cloned_voice = signal.filtfilt(b, a, cloned_voice)

# 3. Save Cloned Audio Output
normalized_audio = (cloned_voice / np.max(np.abs(cloned_voice)) * 32767).astype(np.int16)
wavfile.write(output_path, sample_rate, normalized_audio)
print(f"Cloned audio saved at: {output_path}")

# 4. Plot Comparison
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(t[:500], original_voice[:500], color='blue')
plt.title("Original Audio Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(2, 1, 2)
plt.plot(t[:500], cloned_voice[:500], color='green')
plt.title("Cloned Audio Signal (Pitch & Timbre Modified)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
