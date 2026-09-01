# Multimedia Systems Lab 🎬

> **Summary:**  
> This repository contains the practical implementations, code, and assignments for the **Multimedia Systems Lab**.

---

## 📁 Folder Structure

```text
Geetanshi-IC-2k22-34/
│
├── Cluster01-MMFundamental/        # Multimedia Fundamentals & Sampling
│   ├── new.py                      # Continuous signal generation & sampling demonstration
│   ├── second.py                   # Image loading, metadata extraction & grayscale conversion
│   └── Screenshot *.png            # Output screenshots of plots and images
│
├── cluster02-ImageProcessing/      # Image Processing
│   └── ImgProcessing.py/
│       └── ImageProcessing.py      # Image filtering, transformations & enhancement
│
├── cluster03-AudioProcessing/      # Audio Processing
│   ├── Audio.py                    # Audio file metadata analyzer (using FFprobe)
│   ├── AudioCloning.py             # Voice cloning, acoustic feature extraction & timbre transfer
│   └── WhatsApp Ptt *.opus         # Test audio sample file
│
├── cluster04-Vedio-Analyser/       # Video Analysis
│   └── Vedio.py                    # Video frame extraction and property analysis
│
├── cluster05-Compression/          # Media Compression
│   └── Compression.py              # Lossless and lossy multimedia compression algorithms
│
├── cluster06-MM-coomuncication/    # Multimedia Communication
│   └── ruf.py                      # Media streaming, network transmission & socket tasks
│
├── cluster07-Interective-MM/       # Interactive Multimedia
│   └── ruf.py                      # Interactive controls and media synchronization
│
├── Cluster08-Advance-Multimedia-AI/# Advanced Multimedia AI
│   └── adv.py                      # Artificial Intelligence and Machine Learning in multimedia
│
├── capstone/                       # Final Capstone Project
│
├── dataSet/                        # Test media assets (Audio, Images, Video)
│   ├── AudioFile.mp3
│   ├── flower.jpg
│   ├── flower2.jpg
│   └── voiceover.mp4
│
└── docs/                           # Project documentation, diagrams & experimental results
```

---

## 📑 File & Folder Descriptions

### 1. Cluster01-MMFundamental
* **`new.py`**: Generates a continuous 5 Hz sinusoidal signal, samples it across multiple sampling frequencies (100 Hz, 20 Hz, 10 Hz, 5 Hz), and demonstrates the Nyquist sampling theorem along with signal reconstruction.
* **`second.py`**: Loads an image using OpenCV, extracts image metadata (shape, dimensions, data type, min/max pixel values), converts it from RGB/BGR to Grayscale, and plots the side-by-side comparison using Matplotlib.
* **Screenshots**: Visual output plots of the sampled waveforms and image processing results.

---

### 2. cluster02-ImageProcessing
* **`ImageProcessing.py`**: Implements digital image manipulation tasks such as spatial filtering, image enhancement, and transformations.

---

### 3. cluster03-AudioProcessing
* **`Audio.py`**: Extracts and analyzes detailed audio file metadata using `ffprobe` (including Duration, Bit Rate, Sample Rate, Channels, Codec, and Metadata Tags).
* **`AudioCloning.py`**: Performs voice cloning and timbre transfer by extracting pitch contours ($F_0$), formant/spectral envelopes, and applying spectral morphing to synthesize cloned speech with quantitative evaluation and comparison plots.
* **Sample Audio**: Test voice recording for audio analysis and cloning experiments.

---

### 4. cluster04-Vedio-Analyser
* **`Vedio.py`**: Reads video files to analyze frames, frame rates (FPS), resolution, and visual properties.

---

### 5. cluster05-Compression
* **`Compression.py`**: Implements lossless and lossy data compression techniques for multimedia content.

---

### 6. cluster06-MM-coomuncication
* **`ruf.py`**: Handles multimedia communication experiments including data streaming, protocol simulation, and network socket transmission.

---

### 7. cluster07-Interective-MM
* **`ruf.py`**: Implements interactive multimedia systems, user event handling, and audio-video synchronization.

---

### 8. Cluster08-Advance-Multimedia-AI
* **`adv.py`**: Explores the application of AI and Machine Learning models to multimedia data.

---

### 9. dataSet
Contains test datasets and sample media files used for experiments:
* **`AudioFile.mp3`**: Sample audio recording
* **`flower.jpg` / `flower2.jpg`**: Sample test images
* **`voiceover.mp4`**: Sample video clip

---

### 10. docs & capstone
* **`docs/`**: Contains architectural diagrams, system designs, and experimental logs.
* **`capstone/`**: Dedicated directory for the final lab capstone project.

---

## 🛠️ Prerequisites & Setup

### Requirements
* **Python 3.8+**
* **FFmpeg / FFprobe** (installed and added to system PATH)

### Installation
Install the required Python packages:
```bash
pip install numpy matplotlib opencv-python pillow
```

### Running Experiments
* **Signal Sampling:**
  ```bash
  python Cluster01-MMFundamental/new.py
  ```
* **Image Fundamentals:**
  ```bash
  python Cluster01-MMFundamental/second.py
  ```
* **Audio Metadata Analyzer:**
  ```bash
  python cluster03-AudioProcessing/Audio.py
  ```
* **Voice / Audio Cloning:**
  ```bash
  python cluster03-AudioProcessing/AudioCloning.py
  ```
