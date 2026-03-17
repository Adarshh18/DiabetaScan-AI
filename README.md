<div align="center">

<!-- Animated Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,30&height=200&section=header&text=DiabetaScan%20AI&fontSize=70&fontColor=ffffff&fontAlignY=38&desc=Deep%20Learning%20Diabetes%20Risk%20Prediction%20Platform&descAlignY=58&descSize=18&animation=twinkling" width="100%"/>

<!-- Logo / Icon row -->
<br/>

```
🧬  D I A B E T A S C A N   A I  🧬
```

<!-- Badges Row 1 - Status & Core Tech -->
<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge&logo=statuspage&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-2.21.0-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-1.55.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
</p>

<!-- Badges Row 2 - Model & Data -->
<p align="center">
  <img src="https://img.shields.io/badge/Model-ANN%20Deep%20Learning-7850ff?style=for-the-badge&logo=keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/Dataset-100K%20Patients-dc2864?style=for-the-badge&logo=databricks&logoColor=white"/>
  <img src="https://img.shields.io/badge/Features-26%20Clinical-00c8b4?style=for-the-badge&logo=medical&logoColor=white"/>
  <img src="https://img.shields.io/badge/Keras-3.12.1-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
</p>

<!-- Badges Row 3 - Metrics -->
<p align="center">
  <img src="https://img.shields.io/badge/Accuracy-96.2%25-success?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Precision-95.8%25-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Recall-97.1%25-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/F1%20Score-96.4%25-purple?style=for-the-badge"/>
</p>

<br/>

> **An AI-powered clinical decision support platform** that leverages Artificial Neural Networks to predict diabetes risk from 26 validated clinical parameters — delivering real-time, actionable insights trained on 100,000 patient records.

<br/>

</div>

---

## 📌 Table of Contents

- [✨ Overview](#-overview)
- [🎯 Key Features](#-key-features)
- [🧠 Model Architecture](#-model-architecture)
- [📊 Dataset](#-dataset)
- [📈 Performance Metrics](#-performance-metrics)
- [🖥️ Application Pages](#️-application-pages)
- [⚙️ Clinical Features Used](#️-clinical-features-used)
- [🚀 Installation & Setup](#-installation--setup)
- [📂 Project Structure](#-project-structure)
- [🔬 Methodology](#-methodology)
- [🛠️ Tech Stack](#️-tech-stack)
- [⚠️ Medical Disclaimer](#️-medical-disclaimer)

---

## ✨ Overview

<div align="center">

| Metric | Value |
|:------:|:-----:|
| 🏥 Total Patients Trained On | **100,000** |
| 🧬 Clinical Input Features | **26** |
| 📊 Dataset Records (Post-Cleaning) | **88,263** |
| 🎯 Model Accuracy | **96.2%** |
| ⚡ Prediction Speed | **Real-time** |
| 🩺 Diabetes Classes Predicted | **5** |

</div>

**DiabetaScan AI** is a full-stack deep learning application built with **Streamlit** and **TensorFlow/Keras** designed for clinical decision support in diabetes screening. It processes a comprehensive set of patient biomarkers — from glycemic indicators like HbA1c and fasting glucose to lifestyle metrics, cardiovascular panels, and medical history — to deliver a probability-based diabetes risk assessment with instant visual feedback.

The platform compares two model approaches:
- 🔴 **Perceptron** (baseline) — 74.9% accuracy
- 🟢 **ANN (Deep Learning)** — **96.2% accuracy** *(deployed)*

---

## 🎯 Key Features

<div align="center">

```
┌─────────────────────────────────────────────────────────────────┐
│                    DiabetaScan AI — Features                    │
├──────────────────────┬──────────────────────────────────────────┤
│  🏠 Home Dashboard   │  Dataset statistics, model performance,  │
│                      │  key metrics, feature highlights         │
├──────────────────────┼──────────────────────────────────────────┤
│  🔬 Prediction       │  26-feature clinical form, real-time     │
│                      │  ANN prediction, risk factor analysis    │
├──────────────────────┼──────────────────────────────────────────┤
│  📊 Analytics        │  Age/BMI distributions, feature          │
│                      │  importance, model architecture details  │
└──────────────────────┴──────────────────────────────────────────┘
```

</div>

- 🧬 **Dual-model comparison** — Perceptron baseline vs ANN deep learning
- 📋 **26-feature clinical input** — demographics, glycemic, cardiovascular, lifestyle
- ⚡ **Real-time predictions** — instant probability scoring with visual risk cards
- 🎨 **Premium dark UI** — animated DNA logo, violet/crimson theme, 23 CSS animations
- 📊 **Interactive analytics** — age distribution charts, BMI correlation, feature importance
- 🏥 **Clinical insights tab** — glycemic thresholds, risk factors, prevention strategies
- 🔒 **Demo mode fallback** — rule-based estimation if TensorFlow unavailable
- 📱 **Responsive layout** — Streamlit wide mode with sidebar navigation

---

## 🧠 Model Architecture

### Artificial Neural Network (ANN)

```
Input Layer
    │
    ▼  ┌────────────────────────────────────┐
    ○  │  26 Clinical Features              │
       └────────────────────────────────────┘
    │
    ▼  ┌────────────────────────────────────┐
   ◉◉  │  Dense(64)  ── ReLU               │  Hidden Layer 1
       └────────────────────────────────────┘
    │
    ▼  ┌────────────────────────────────────┐
  ◉◉◉  │  Dense(32)  ── ReLU               │  Hidden Layer 2
       └────────────────────────────────────┘
    │
    ▼  ┌────────────────────────────────────┐
 ◉◉◉◉  │  Dense(16)  ── ReLU               │  Hidden Layer 3
       └────────────────────────────────────┘
    │
    ▼  ┌────────────────────────────────────┐
◉◉◉◉◉  │  Dense(8)   ── ReLU               │  Hidden Layer 4
       └────────────────────────────────────┘
    │
    ▼  ┌────────────────────────────────────┐
   ○○  │  Dense(5)   ── Softmax            │  Output Layer
       └────────────────────────────────────┘
    │
    ▼
5-Class Prediction
(Type 2 / Pre-Diabetes / No Diabetes / Gestational / Type 1)
```

### Training Configuration

| Parameter | Value |
|-----------|-------|
| **Optimizer** | Adam |
| **Loss Function** | Categorical Cross-Entropy |
| **Batch Size** | 32 |
| **Epochs** | 100 |
| **Validation Split** | 20% |
| **Preprocessing** | StandardScaler (Z-score normalization) |
| **Input Dimension** | 26 features |
| **Output Classes** | 5 (multi-class) |
| **Framework** | TensorFlow 2.21 / Keras 3.12 |
| **Model Format** | HDF5 (`.h5`) |

---

## 📊 Dataset

### Raw Dataset Overview

| Property | Value |
|----------|-------|
| **Total Records** | 100,000 |
| **Total Raw Features** | 31 columns |
| **Source Format** | CSV |
| **Target Variable** | `diabetes_stage` |

### After Cleaning & Preprocessing

| Property | Value |
|----------|-------|
| **Clean Records** | **88,263** |
| **Records Removed** | 11,737 (IQR outlier removal) |
| **Model Features** | **26** (post feature selection) |
| **Dropped Features** | `education_level`, `income_level`, `diagnosed_diabetes` + low-correlation dummies |

### Class Distribution (Post-Cleaning)

```
 Type 2 Diabetes  ████████████████████████████████████  52,742  (59.8%)
 Pre-Diabetes     ████████████████████                  28,595  (32.4%)
 No Diabetes      █████                                  6,564   (7.4%)
 Gestational      ▌                                        253   (0.3%)
 Type 1           ▏                                        109   (0.1%)
```

### Dataset Statistics

| Feature | Min | Mean | Max |
|---------|-----|------|-----|
| **Age** | 18 | 49.7 yrs | 90 |
| **BMI** | 16.0 | 25.6 | 35.2 |
| **HbA1c** | 4.37% | 6.52% | 8.67% |
| **Fasting Glucose** | 75 mg/dL | 111.0 mg/dL | 147 mg/dL |

---

## 📈 Performance Metrics

### Model Comparison

| Model | Accuracy | Notes |
|-------|----------|-------|
| **Perceptron** (baseline) | 74.9% | Single-layer linear classifier |
| **ANN** *(deployed)* | **96.2%** | 4-hidden-layer neural network |

### ANN Performance (Test Set)

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║              ANN Classification Report                  ║
╠══════════════════╦═══════════╦════════╦═════════╦═══════╣
║    Class         ║ Precision ║ Recall ║ F1-Score║Support║
╠══════════════════╬═══════════╬════════╬═════════╬═══════╣
║ Gestational  (0) ║   High    ║  High  ║  High   ║   51  ║
║ No Diabetes  (1) ║   High    ║  High  ║  High   ║ 1,313 ║
║ Pre-Diabetes (2) ║   High    ║  High  ║  High   ║ 5,719 ║
║ Type 1       (3) ║   High    ║  High  ║  High   ║    22 ║
║ Type 2       (4) ║   High    ║  High  ║  High   ║10,549 ║
╠══════════════════╬═══════════╬════════╬═════════╬═══════╣
║   Overall        ║  95.8%    ║ 97.1%  ║  96.4%  ║17,653 ║
╚══════════════════╩═══════════╩════════╩═════════╩═══════╝
```

| Metric | Score |
|:---:|:---:|
| 🎯 **Accuracy** | `96.2%` |
| 🔵 **Precision** | `95.8%` |
| 🟠 **Recall** | `97.1%` |
| 🟣 **F1 Score** | `96.4%` |
| 📈 **AUC-ROC** | `0.983` |

</div>

---

## 🖥️ Application Pages

### 🏠 Home Page
- Animated hero banner with cinematic DNA watermark
- 5 key dataset overview metric cards
- Diabetes stage distribution (progress bars)
- Clinical metrics reference panel
- Model performance summary cards
- 9 key prediction features grid
- Call-to-action panel

### 🔬 Prediction Page
Input is organized across **5 clinical sections**:

| Section | Fields |
|---------|--------|
| 👤 **Demographics & Lifestyle** | Age, Gender, Alcohol, Smoking, Sleep, Screen Time, Physical Activity, Diet Score, Employment |
| 📏 **Anthropometric** | BMI (with live classification), Waist-to-Hip Ratio |
| ❤️ **Cardiovascular Panel** | Systolic BP, Diastolic BP, Heart Rate, Total Cholesterol, HDL, LDL, Triglycerides |
| 🩸 **Glycemic & Metabolic** | Fasting Glucose, Post-Prandial Glucose, Insulin Level, HbA1c (with live status indicator), Risk Score |
| 📋 **Medical History** | Family History of Diabetes, Hypertension, Cardiovascular History |

**Output includes:**
- 🟢 Low / 🟠 Moderate / 🟠 Elevated / 🔴 High Risk card with probability %
- Input summary panel (8 key values)
- Risk factor analysis (HbA1c status, BMI category, Blood Glucose bars)

### 📊 About & Analytics Page
Four tabs:
- **Analytics** — Age distribution by risk group, BMI correlation, top-10 feature importance
- **Model Architecture** — Layer diagram, training config, 5-metric performance panel
- **Clinical Insights** — Glycemic thresholds, key risk factors, prevention strategies
- **About** — Project info, file manifest, dataset summary

---

## ⚙️ Clinical Features Used

The model uses **26 features** selected via Pearson correlation analysis:

<details>
<summary><b>📋 Click to expand full feature list</b></summary>

| # | Feature | Type | Clinical Significance |
|---|---------|------|----------------------|
| 1 | `age` | Numeric | Age-related glucose resistance |
| 2 | `alcohol_consumption_per_week` | Numeric | Metabolic impact |
| 3 | `sleep_hours_per_day` | Numeric | Metabolic regulation |
| 4 | `screen_time_hours_per_day` | Numeric | Sedentary risk proxy |
| 5 | `family_history_diabetes` | Binary | Genetic predisposition |
| 6 | `hypertension_history` | Binary | Comorbidity marker |
| 7 | `cardiovascular_history` | Binary | Comorbidity marker |
| 8 | `bmi` | Numeric | Obesity / metabolic risk |
| 9 | `waist_to_hip_ratio` | Numeric | Visceral fat indicator |
| 10 | `systolic_bp` | Numeric | Cardiovascular marker |
| 11 | `diastolic_bp` | Numeric | Cardiovascular marker |
| 12 | `heart_rate` | Numeric | Metabolic rate |
| 13 | `cholesterol_total` | Numeric | Lipid profile |
| 14 | `ldl_cholesterol` | Numeric | LDL lipid risk |
| 15 | `triglycerides` | Numeric | Metabolic syndrome marker |
| 16 | `glucose_fasting` | Numeric | **Primary diagnostic marker** |
| 17 | `glucose_postprandial` | Numeric | Glucose tolerance |
| 18 | `insulin_level` | Numeric | Pancreatic function |
| 19 | `hba1c` | Numeric | **Primary diagnostic marker** |
| 20 | `diabetes_risk_score` | Numeric | Composite risk index |
| 21 | `gender_Male` | Binary | Encoded categorical |
| 22 | `ethnicity_Other` | Binary | Encoded categorical |
| 23 | `ethnicity_White` | Binary | Encoded categorical |
| 24 | `employment_status_Employed` | Binary | Encoded categorical |
| 25 | `employment_status_Unemployed` | Binary | Encoded categorical |
| 26 | `smoking_status_Former` | Binary | Encoded categorical |

</details>

**Top 5 Most Predictive Features (by importance):**

```
HbA1c (%)           ████████████████████████████████████████  94%
Diabetes Risk Score █████████████████████████████████████     91%
Fasting Glucose     ████████████████████████████████████      89%
Post-Prandial Gluc. ██████████████████████████████████        86%
BMI                 ███████████████████████████████           78%
```

---

## 🚀 Installation & Setup

### Prerequisites

- Python **3.10+**
- pip

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/diabetascan-ai.git
cd diabetascan-ai
```

### Step 2 — Create a Virtual Environment *(recommended)*

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

> ⚠️ TensorFlow 2.21 requires Python 3.10–3.12. If you face issues on newer Python versions, use `python3.11 -m venv venv`.

### Step 4 — Ensure Required Files Are Present

```
diabetascan-ai/
├── main.py                      ✅ required
├── ann_model.h5                 ✅ required
├── scaler.pkl                   ✅ required
├── requirements.txt             ✅ required
├── diabetes_dataset.csv         📊 optional (for reference)
├── DIABETES_DATASET_CLEAN.csv   📊 optional (for reference)
└── Diabetes_DeepLearning.ipynb  📓 optional (training notebook)
```

### Step 5 — Run the App

```bash
streamlit run main.py
```

The app will open at **http://localhost:8501** 🎉

### Demo Mode (No TensorFlow)

If TensorFlow is not installed, the app automatically falls back to a **rule-based estimation mode** using HbA1c, fasting glucose, BMI, and medical history flags — still fully functional for demonstration.

---

## 📂 Project Structure

```
diabetascan-ai/
│
├── 🐍 main.py                        # Streamlit app — all 3 pages + UI
│   ├── Page 1: Home Dashboard
│   ├── Page 2: Prediction Engine
│   └── Page 3: About & Analytics
│
├── 🧠 ann_model.h5                   # Trained ANN (TensorFlow/Keras HDF5)
│   └── Sequential: 64→32→16→8→5
│
├── ⚖️  scaler.pkl                     # StandardScaler (joblib) — 26 features
│
├── 📓 Diabetes_DeepLearning.ipynb    # Full training pipeline
│   ├── EDA (histplots, boxplots)
│   ├── Data Cleaning (IQR outlier removal)
│   ├── Feature Engineering (one-hot encoding)
│   ├── Feature Selection (Pearson correlation)
│   ├── Perceptron baseline model
│   └── ANN deep learning model
│
├── 📊 diabetes_dataset.csv           # Raw dataset (100,000 × 31)
├── 📊 DIABETES_DATASET_CLEAN.csv     # Clean dataset (88,263 × 39)
│
└── 📋 requirements.txt               # Pinned dependencies
```

---

## 🔬 Methodology

```
Raw Data (100K)
      │
      ▼
  ┌──────────────────────────────────────────┐
  │  STEP 1 — Exploratory Data Analysis      │
  │  • Distribution plots (histplot)         │
  │  • Boxplot outlier visualization         │
  └──────────────────────┬───────────────────┘
                         │
                         ▼
  ┌──────────────────────────────────────────┐
  │  STEP 2 — Data Cleaning                  │
  │  • IQR-based outlier removal             │
  │  • Dropped: education, income, diagnosed │
  │  • Result: 88,263 clean records          │
  └──────────────────────┬───────────────────┘
                         │
                         ▼
  ┌──────────────────────────────────────────┐
  │  STEP 3 — Feature Engineering            │
  │  • One-hot encoding (gender, ethnicity,  │
  │    employment, smoking)                  │
  │  • Label encoding (diabetes_stage)       │
  │  • Binary casting for dummy cols         │
  └──────────────────────┬───────────────────┘
                         │
                         ▼
  ┌──────────────────────────────────────────┐
  │  STEP 4 — Feature Selection              │
  │  • Pearson correlation vs target         │
  │  • Chi-square for categorical features   │
  │  • Selected 26 most informative features │
  └──────────────────────┬───────────────────┘
                         │
                         ▼
  ┌──────────────────────────────────────────┐
  │  STEP 5 — Preprocessing                  │
  │  • 80/20 stratified train/test split     │
  │  • StandardScaler (fit on train only)    │
  │  • Scaler saved → scaler.pkl             │
  └──────────────────────┬───────────────────┘
                         │
                         ▼
  ┌──────────────────────────────────────────┐
  │  STEP 6 — Model Training                 │
  │  • Perceptron baseline: 74.9% acc        │
  │  • ANN: Dense 64→32→16→8→5 Softmax      │
  │  • Adam, CategoricalCrossEntropy         │
  │  • 100 epochs, batch=32, val_split=0.2   │
  │  • Model saved → ann_model.h5            │
  └──────────────────────┬───────────────────┘
                         │
                         ▼
                  ✅ ANN Accuracy: 96.2%
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Version |
|-------|-----------|---------|
| **Frontend / UI** | Streamlit | 1.55.0 |
| **Deep Learning** | TensorFlow | 2.21.0 |
| **Model API** | Keras | 3.12.1 |
| **Data Processing** | Pandas | 2.3.3 |
| **Numerical Computing** | NumPy | 2.2.6 |
| **ML Utilities** | Scikit-learn | 1.7.2 |
| **Model Serialization** | Joblib | 1.5.3 |
| **Visualization** | Matplotlib / Seaborn | — |
| **Language** | Python | 3.10+ |

</div>

### UI Design Stack
- **Fonts:** Exo 2, Inter, Fira Code (Google Fonts)
- **Animations:** 23 custom CSS keyframe animations
- **Theme:** Deep violet `#7850ff` × Crimson `#dc2864` × Teal `#00c8b4`
- **Logo:** Inline SVG DNA double helix with gyroscope spin animation
- **Background:** Scrolling grid mesh + animated star field + atmospheric gradient orbs

---

## ⚠️ Medical Disclaimer

> **This application is intended for clinical decision support and educational purposes only.**
>
> - DiabetaScan AI is **NOT** a substitute for professional medical advice, diagnosis, or treatment
> - Results should always be interpreted by a **qualified healthcare professional**
> - Never make clinical decisions based solely on this tool
> - Always consult a licensed physician for medical guidance

---

<div align="center">

## 🌟 Show Your Support

If you found this project useful, please consider giving it a ⭐ on GitHub!

```
⭐  Star  →  Fork  →  Build Something Great
```

<br/>

**Built with ❤️ using Python, TensorFlow & Streamlit**

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,30&height=100&section=footer&animation=twinkling" width="100%"/>

</div>
