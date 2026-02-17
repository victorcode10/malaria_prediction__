# 🦟 Malaria Risk Prediction - Installation Guide

## Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the App
```bash
streamlit run app/app.py
```

### Step 3: Open in Browser
The app will automatically open at `http://localhost:8501`

---

## Troubleshooting

### If you see: "PyCaret only supports python 3.9, 3.10, 3.11"

**The app includes an automatic patcher**, but if it fails due to permissions:

#### Option A: Run the manual patch (Recommended)
```bash
python patch_pycaret.py --force
```

#### Option B: Use sudo/admin privileges (Linux/Mac)
```bash
sudo python patch_pycaret.py --force
```

#### Option C: Manual edit (if above fails)
1. Find your PyCaret installation:
   ```bash
   python -c "import pycaret; print(pycaret.__file__)"
   ```

2. Open that `__init__.py` file in a text editor

3. Find line 21 (around line 21):
   ```python
   elif sys.version_info >= (3, 12):
   ```

4. Change it to:
   ```python
   elif False: # sys.version_info >= (3, 12):
   ```

5. Save and run the app again

---

## System Requirements

- **Python**: 3.9, 3.10, 3.11, or 3.12
- **OS**: Windows, macOS, or Linux
- **RAM**: Minimum 4GB (8GB recommended)
- **Disk Space**: ~500MB for dependencies

---

## Dependencies Installed

- streamlit 1.40.0
- pycaret 3.3.2
- pandas 2.2.0
- numpy 1.26.4
- scikit-learn 1.5.1
- Plus their sub-dependencies

---

## Using the App

1. **Fill in Patient Information** (left sidebar):
   - Age
   - Temperature
   - Region in Nigeria
   - Season

2. **Environmental Factors**:
   - Lives near water?
   - Uses mosquito net?
   - Previous malaria cases

3. **Clinical Symptoms**:
   - Days of fever
   - Headache, chills, fatigue, etc.

4. **Lab Results**:
   - Red blood cell count
   - White blood cell count

5. **Click "Predict Malaria Risk"**

The app will display:
- Risk prediction (Positive/Negative)
- Confidence score
- Recommended actions
- Risk factor analysis

---

## Deployment Options

### Local Development
```bash
streamlit run app/app.py
```

### Streamlit Cloud
1. Push to GitHub
2. Connect at share.streamlit.io
3. Deploy from repository

### Docker (Coming Soon)
```bash
docker build -t malaria-predictor .
docker run -p 8501:8501 malaria-predictor
```

---

## Project Structure

```
malaria-risk-prediction/
├── app/
│   ├── app.py                    # Main Streamlit application
│   └── patch_pycaret.py          # Auto-patcher for Python 3.12
├── models/
│   └── malaria_risk_model.pkl    # Trained ML model
├── data/
│   └── malaria_risk_dataset.csv  # Training dataset
├── notebook/
│   └── malaria_risk_prediction.ipynb  # Model training notebook
├── requirements.txt              # Python dependencies
├── patch_pycaret.py              # Standalone patcher
├── FIXES_APPLIED.md              # Fix documentation
└── INSTALLATION.md               # This file
```

---

## Support

### Common Issues

**Import Error: No module named 'pycaret'**
```bash
pip install pycaret==3.3.2
```

**Streamlit not found**
```bash
pip install streamlit==1.40.0
```

**Model file not found**
- Ensure you're in the project root directory
- Check that `models/malaria_risk_model.pkl` exists

**Permission denied when patching**
- Run with sudo/admin: `sudo python patch_pycaret.py --force`
- Or follow Option C for manual editing

---

## About This Project

This is an AI-powered medical decision support tool for malaria screening in Nigerian healthcare settings. The model was trained on synthetic data representing malaria risk patterns across Nigerian regions.

**⚠️ Medical Disclaimer**: This tool is for screening purposes only. Positive predictions should be confirmed with laboratory testing (RDT or microscopy). Always consult a healthcare professional for diagnosis and treatment.

---

## Credits

- **Author**: Blossom Academy
- **Course**: Data Science Capstone Projects
- **Model**: Gradient Boosting Classifier (PyCaret)
- **Framework**: Streamlit

---

## License

Educational use only. Not for commercial deployment without proper medical validation.
