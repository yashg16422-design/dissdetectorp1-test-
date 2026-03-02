# 🩺 ClinicalDetec_: Real-Time Patient Deterioration Detection

ClinicalDetec_ is a **GPU-accelerated PyTorch project** for detecting **early patient deterioration** from **streaming physiological time-series data** using a **Transformer-based temporal model**.

The system is designed to resemble **real clinical monitoring pipelines**, emphasizing **streaming inference**, **bounded memory**, and **production-style ML engineering** rather than offline-only experimentation.

> ⚠️ This project is intended for **educational and research purposes only** and must not be used for clinical decision-making.

---

## 🚑 Problem Statement

In hospital and ICU environments, patients are continuously monitored through vital signs such as:

- Heart rate  
- Blood pressure  
- Body temperature  
- Oxygen saturation  
- Other physiological signals  

Patient deterioration often develops gradually and is reflected in **temporal patterns**, not isolated abnormal measurements.

This project focuses on:
- Modeling **temporal dependencies** in multivariate physiological signals
- Detecting abnormal trends **early**
- Supporting **real-time inference** on streaming data

---

## 🧠 Methodology

### Temporal Modeling
- A **Transformer encoder** processes fixed-length windows of multivariate time-series data
- Self-attention captures both short- and long-range temporal dependencies
- The model predicts physiological behavior over the window

### Deterioration Signal
- A **risk score** is computed from prediction error
- Higher deviation from expected temporal behavior indicates increased deterioration risk

This mirrors approaches used in real-world patient monitoring and predictive maintenance systems.

---

## 🔁 Sliding-Window Inference

The system operates on **streaming data** using a sliding-window mechanism:

- A rolling buffer stores the most recent `N` timesteps
- Each new measurement updates the buffer
- Inference is triggered once the buffer is full
- Memory usage remains constant over time

This enables **near-real-time risk updates** and reflects realistic deployment constraints.

---

## ⚡ GPU Acceleration (CUDA)

CUDA acceleration is used where it provides meaningful benefit:

- Transformer self-attention
- Batched sequence processing
- Streaming inference over long-running data streams

The project includes:
- Automatic device selection (CPU / GPU)
- Explicit CPU vs GPU latency benchmarking
- GPU-safe inference with minimal data transfers

---

The repository follows a **modular, production-style layout** with clear separation between data handling, modeling, training, inference, and benchmarking.

---

## 🧪 Data

- Includes a **synthetic physiological data generator**
- Simulates multivariate patient vital signs with gradual deterioration trends
- CSV-based interface allows easy replacement with real-world datasets

No proprietary or restricted datasets are required.

---
Afetr Cloning the Repo
## 🚀 Usage

### Install dependencies
```bash
pip install -r requirements.txt
python data/synthetic_generator.py
```
## Train the model
```
python training/train.py
```

Run real-time inference
```
python inference/realtime_monitor.py
```
Benchmark CPU vs GPU performance
```
python benchmarks/gpu_latency.py
```
