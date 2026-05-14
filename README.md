# 🎲 Mega Millions Mega Ball Predictor

A deep learning application that predicts the **Mega Ball** number in the Mega Millions lottery based on historical drawing data. Built with **TensorFlow** and **Streamlit**, the project features a fully trained neural network served through an interactive web interface.

---

## 📋 Project Summary

This end-to-end machine learning project demonstrates the full ML lifecycle:

1. **Data ingestion** — 2,419 historical Mega Millions draw results parsed from CSV
2. **Feature engineering** — Multi-hot encoding transforms the 5 white-ball numbers into a 75-dimensional input vector
3. **Model training** — A 3-layer feedforward neural network trained via Keras to predict the Mega Ball (1–25)
4. **Model serving** — A lightweight Streamlit web app loads the trained `.keras` model and makes real-time predictions
5. **Visualization** — Probability distribution bar chart for all 25 possible Mega Ball values

---

## 🛠️ Tech Stack

| Component               | Technology                           |
|-------------------------|--------------------------------------|
| **Deep Learning**       | TensorFlow / Keras (Sequential API)  |
| **Web App**             | Streamlit                            |
| **Language**            | Python 3.12                          |
| **Data Processing**     | NumPy, Pandas                        |
| **Preprocessing**       | scikit-learn (train/test split)      |
| **Model Format**        | Keras `.keras` (native)              |
| **Notebook**            | Jupyter (model development & EDA)    |

---

## 🧠 How the ML Model Works

### Data Encoding

Each draw consists of 5 white-ball numbers (1–75) and 1 Mega Ball (1–25). The white balls are converted into a **multi-hot binary vector** of length 75:

```
Input example: [1, 2, 3, 4, 5]
Multi-hot:     [1, 1, 1, 1, 1, 0, 0, ..., 0]  (length 75)
```

The Mega Ball target is **one-hot encoded** into 25 classes.

### Neural Network Architecture

```
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Layer                 ┃ Neurons    ┃ Parameters┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ Dense (ReLU)          │ 128        │     9,728 │
│ Dense (ReLU)          │ 64         │     8,256 │
│ Dense (Softmax)       │ 25         │     1,625 │
└───────────────────────┴────────────┴───────────┘
Total params: ~21,400 (83 KB)
```

- **Optimizer**: Adam
- **Loss**: Categorical Crossentropy
- **Batch size**: 32
- **Epochs**: 30
- **Train / Validation / Test split**: 76.5% / 8.5% / 15%

### Prediction Flow

1. User picks 5 white-ball numbers (1–75) via the Streamlit sidebar
2. The app builds a multi-hot vector from the selection
3. The trained model computes softmax probabilities across all 25 Mega Ball classes
4. The class with highest probability is shown as the **predicted Mega Ball**
5. A bar chart visualizes the full probability distribution

---

## 📸 Demo / Screenshots

Run the app locally to see the interface in action:

![Mega Millions Predictor Screenshot](https://i.imgur.com/placeholder-demo.png)

*Streamlit sidebar with white-ball selector, prediction result, and probability bar chart.*

> **Coming soon:** Animated GIF walkthrough and live Streamlit Cloud deployment link.

---

## 🚀 Setup Instructions

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/trayp20/Mega-Millions.git
cd Mega-Millions

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

The app will automatically load the pre-trained model (`megaball_model.keras`). Use the sidebar to select 5 white-ball numbers and click **"Predict Mega Ball"**.

### Reproduce Training

Open `lottery.ipynb` in Jupyter to see the full data pipeline, model architecture, training loop, and evaluation:

```bash
jupyter notebook lottery.ipynb
```

---

## 📊 Results & Accuracy Discussion

### Test Set Performance

The model achieves **~4.1% test accuracy** on a held-out set of ~363 draws (15% of data).

### Context & Interpretation

| Metric | Value | Notes |
|--------|-------|-------|
| **Random baseline** | ~4.0% (1/25) | Pure chance across 25 equally-likely classes |
| **Model test accuracy** | ~4.1% | Marginally above random |
| **Training accuracy** | ~63% | After 30 epochs (overfitting) |
| **Validation accuracy** | ~3–5% | Stable at baseline throughout training |

### Key Insight: This Problem Is Inherently Unpredictable

Lottery draws are designed to be **independent, uniformly random events**. The model's performance being essentially equal to random chance is **the expected outcome** — and a valuable demonstration of why machine learning cannot beat true randomness.

**What the project demonstrates to recruiters:**

- ✅ End-to-end ML pipeline design and implementation
- ✅ Proper train/validation/test methodology (detecting overfitting)
- ✅ Multi-hot encoding for categorical feature representation
- ✅ Model serialization and deployment in a web UI
- ✅ Honest evaluation and interpretation of results
- ✅ Clean, modular Python code with Keras + Streamlit

### Overfitting Pattern

The widening gap between training accuracy (rising to ~63%) and validation accuracy (staying ~4%) shows classic overfitting — the model memorizes training patterns that don't generalize. This is expected: since each draw is independent, there are no learnable patterns in the data.

---

## 📁 Repository Structure

```
Mega-Millions/
├── app.py                              # Streamlit web application
├── lottery.ipynb                       # Jupyter notebook (training & EDA)
├── megaball_model.keras                # Pre-trained Keras model
├── Lottery_Mega_Millions_Winning_Numbers.csv  # Historical dataset (2,419 draws)
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
└── LICENSE                             # MIT License
```

---

## 📄 License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---

*Built with TensorFlow, Streamlit, and Python. A portfolio project demonstrating applied deep learning — even when the problem is inherently unsolvable, the engineering is real.*
