# Malaria Risk Prediction

An AI-powered medical screening tool to predict malaria infection risk in Nigerian patients using machine learning.

---

## Problem Statement

Malaria is Nigeria's leading cause of death, accounting for **27% of global malaria cases**. Early detection is critical, but laboratory testing isn't always immediately available in rural areas. This ML model provides **rapid risk assessment** to guide healthcare decisions while awaiting confirmatory tests.

---

## Objectives

- Predict malaria infection risk from symptoms and demographics  
- Support clinical decision-making in resource-limited settings  
- Enable rapid screening at primary healthcare centers  
- Reduce diagnostic delays in rural areas  

---

## Dataset

**Number of records:** 4000 patient entries  

**Features include:**

- **Demographics:** Age, region  
- **Environmental:** Season, water proximity, mosquito net usage  
- **Clinical:** Temperature, fever duration, symptoms (headache, chills, fatigue, vomiting, appetite loss)  
- **Laboratory:** Red blood cell (RBC) count, white blood cell (WBC) count  
- **History:** Previous malaria cases  

**Target variable:** `malaria_positive` (0 = Negative, 1 = Positive)  

---

## Installation

```bash
# Clone the repository
cd malaria-risk-prediction

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux / Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## Training the Model

```bash
python train.py
```

**Output:** `malaria_risk_model.pkl`  

---

## Running the App

```bash
streamlit run app.py
```

Navigate to: http://localhost:8501  

---

## Deployment

### GitHub

```bash
git init
git add .
git commit -m "Malaria prediction model"
git remote add origin https://github.com/your-username/malaria-risk-prediction.git
git push -u origin main
```

### Streamlit Cloud

1. Go to https://share.streamlit.io  
2. Connect your GitHub repository  
3. Set main file to `app.py`  
4. Deploy  

---

## Medical Disclaimer

This tool is for **screening purposes only**. All positive predictions must be confirmed with:

- Rapid Diagnostic Test (RDT)  
- Microscopy examination  

Always consult qualified healthcare professionals for diagnosis and treatment.

---

## Model Performance Metrics

After training, evaluate:

- **Accuracy**  
- **F1-Score** (primary metric for malaria prediction)  
- **Recall**  
- **AUC**  

> F1 is prioritized because balanced detection of positive and negative cases is critical for malaria screening. Accuracy is checked as a backup since the dataset is balanced (50% positive, 50% negative).

---

## Project Tips

1. Understand the medical context – read about malaria symptoms  
2. Feature importance – identify which symptoms are most predictive  
3. Balance sensitivity vs specificity – missing a malaria case is worse than a false alarm  
4. Test edge cases – very young patients, high fever, multiple symptoms  

---

## Learning Resources

- WHO Malaria Guidelines  
- Nigeria Malaria Indicator Survey  
- PyCaret Classification Documentation
