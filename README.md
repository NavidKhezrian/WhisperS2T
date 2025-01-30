Here's an even better **README.md**, enhancing clarity, structure, and user-friendliness:

---

# **WhisperS2T Setup Guide**

## **Overview**

**WhisperS2T** is an optimized **speech-to-text** solution based on OpenAI's **Whisper** model, offering improved efficiency for **transcribing audio**.

### **Original Repository**

🔗 [WhisperS2T by shashikg](https://github.com/shashikg/WhisperS2T)

---

## **Prerequisites**

Before installing **WhisperS2T**, ensure you have the following:

✅ **Anaconda** installed on your system\
✅ **A compatible NVIDIA GPU** (for CUDA acceleration)\
✅ **NVIDIA CUDA Toolkit (12.1)** – [Download CUDA 12.1](https://developer.nvidia.com/cuda-12-1-0-download-archive)\
✅ **NVIDIA cuDNN Library (12.1)**\
✅ **FFmpeg** 

---

## **Installation Steps**

### **1. Clone the Repository**

```sh
git clone https://gitlab.hs-coburg.de/fei-mr-lab/whisper-s2t.git
cd whisper-s2t
```

### **2. Create and Activate a Conda Environment**

```sh
conda create -n whisperS2T python=3.10 -y
conda activate whisperS2T
```

### **3. Install FFmpeg**

FFmpeg is required for audio processing. Install it based on your operating system:

- **Windows:** [FFmpeg Installation Guide](https://phoenixnap.com/kb/ffmpeg-windows)


**Verify installation:**

Run the following command to check if FFmpeg is installed correctly:

```sh
ffmpeg -version
```

If installed properly, it will display FFmpeg version details.

### **4. Install PyTorch with CUDA (for GPU Acceleration)**

For **GPU support**, install PyTorch and dependencies:

```sh
conda install pytorch=2.1.2 torchvision=0.16.2 torchaudio=2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia
```

### **5. Install WhisperS2T**

Now, install **WhisperS2T** using **pip**:

```sh
pip install -U whisper-s2t
```

---

## **Running WhisperS2T**

To start the **WhisperS2T** application, run:

```sh
python app.py
```

Once the server is running, open the following address in your browser:

🌍 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## **Additional Resources**

For advanced configurations, documentation, and further details, visit:\
🔗 **[WhisperS2T GitHub Repository](https://github.com/shashikg/WhisperS2T)**

---


