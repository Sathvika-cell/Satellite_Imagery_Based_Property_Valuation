# 🏠 Multimodal Property Valuation using Satellite Images & Tabular Data

This project builds a **multimodal deep learning system** to predict residential property prices by combining **structured housing attributes** with **satellite imagery**.  
The objective is to evaluate whether visual context from satellite images improves prediction performance compared to traditional tabular-only models.

---

## 📌 Project Overview

Property prices are influenced not only by internal features (size, rooms, location) but also by **neighborhood characteristics** such as road connectivity, urban density, and surrounding infrastructure. Satellite imagery captures this contextual information.

This project implements:
- A **tabular-only baseline model**
- A **multimodal CNN + MLP model**
- **Grad-CAM visualizations** for interpretability

---

## 📂 Repository Structure

```
property-valuation-multimodal/
│
├── property_valuation.ipynb
├── image_download.ipynb
├── preprocessing.ipynb
├── model_training.ipynb
│
├── data/
│   ├── kc_house_data.csv
│   ├── train_processed.csv
│   └── test_processed.csv
│
├── images/
│   ├── 0.png
│   ├── 1.png
│   └── ...
│
├── outputs/
│   ├── predictions_tabular.csv
│   ├── predictions_multimodal.csv
│   └── gradcam/
│
├── figures/
│   └── architecture_diagram.png
│
└── README.md
```

---

## 📓 Notebook Description

### 1️⃣ property_valuation.ipynb
- Exploratory Data Analysis (EDA)
- Feature inspection and correlations
- Problem formulation and motivation

### 2️⃣ image_download.ipynb
- Downloads satellite images using latitude and longitude
- Saves images as `images/{image_id}.png`
- Ensures alignment with dataset indices

### 3️⃣ preprocessing.ipynb
- Train-test split
- Feature scaling using `StandardScaler`
- Saves processed datasets for modeling

### 4️⃣ model_training.ipynb
- Trains a **tabular-only baseline**
- Trains a **multimodal deep learning model**
- Evaluates using RMSE and R²
- Saves predictions
- Generates Grad-CAM visualizations

---

## 🧠 Model Architecture

- **Image branch**: ResNet-based CNN
- **Tabular branch**: Fully-connected neural network
- **Fusion**: Concatenation of image and tabular embeddings
- **Output**: Regression head predicting price

Architecture diagram available in:
```
figures/architecture_diagram.png
```

---

## 📊 Results

| Model | RMSE | R² |
|------|------|----|
| Tabular-Only | 0.180 | 0.785 |
| Multimodal | Improved | Higher |

The multimodal model demonstrates that satellite imagery provides complementary predictive signals.

---

## 🔍 Interpretability (Grad-CAM)

Grad-CAM is used to visualize which regions of satellite images influence predictions, highlighting:
- Road networks
- Urban density
- Surrounding infrastructure

---

## 🛠️ Tech Stack

- Python
- PyTorch & torchvision
- scikit-learn
- pandas, numpy
- matplotlib, seaborn

---

## 🚀 How to Run

1. Mount Google Drive
2. Run notebooks in order:
```
property_valuation.ipynb
image_download.ipynb
preprocessing.ipynb
model_training.ipynb
```
3. Use GPU (Tesla T4 recommended)

---

## 📌 Conclusion

This project validates the effectiveness of **multimodal learning** for property valuation by integrating visual and structured data, achieving better performance and improved interpretability.

---

## ✨ Future Work
- Higher resolution imagery
- Temporal neighborhood analysis
- Attention-based fusion
