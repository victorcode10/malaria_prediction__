"""
MALARIA RISK PREDICTION - STREAMLIT APP
========================================
A medical decision support tool to predict malaria infection risk.

Author: Blossom Academy
Course: Data Science Capstone Projects
"""

# Auto-patch PyCaret for Python 3.12 compatibility
import sys
import os

# Add the app directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Try to patch PyCaret before importing it
try:
    from patch_pycaret import patch_pycaret
    patch_pycaret()
except Exception as e:
    print(f"Warning: Could not auto-patch PyCaret: {e}")

import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# Page config
st.set_page_config(
    page_title="Malaria Risk Predictor",
    page_icon="🦟",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #D32F2F;
        text-align: center;
        font-weight: bold;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .positive-result {
        background-color: #ffebee;
        padding: 2rem;
        border-radius: 10px;
        border-left: 5px solid #D32F2F;
        margin: 1rem 0;
    }
    .negative-result {
        background-color: #e8f5e9;
        padding: 2rem;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #FF9800;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-title">🦟 Malaria Risk Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-Powered Malaria Screening for Nigerian Healthcare</p>', unsafe_allow_html=True)

# Medical disclaimer
st.markdown("""
    <div class="warning-box">
        ⚠️ <strong>Medical Disclaimer:</strong> This tool is for screening purposes only. 
        A positive prediction should be confirmed with laboratory testing (RDT or microscopy).
        Always consult a healthcare professional for diagnosis and treatment.
    </div>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_trained_model():
    import os
    # Get the absolute path to the models directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    models_dir = os.path.join(current_dir, '..', 'models')
    model_path = os.path.join(models_dir, 'malaria_risk_model')
    return load_model(model_path)

model = load_trained_model()

# Sidebar - Patient Information
st.sidebar.header("👤 Patient Information")

age = st.sidebar.number_input("Age (years)", min_value=1, max_value=100, value=25)

temperature = st.sidebar.number_input(
    "Body Temperature (°C)", 
    min_value=35.0, 
    max_value=42.0, 
    value=37.0,
    step=0.1
)

region = st.sidebar.selectbox(
    "Region in Nigeria",
    ['South_South', 'South_West', 'South_East', 'North_Central', 'North_West', 'North_East']
)

season = st.sidebar.radio(
    "Current Season",
    ['Dry_Season', 'Rainy_Season']
)

# Environmental & Preventive Factors
st.sidebar.header("🌍 Environmental Factors")

lives_near_water = st.sidebar.radio(
    "Lives near stagnant water/swamp?",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

uses_mosquito_net = st.sidebar.radio(
    "Uses mosquito net?",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

previous_malaria_cases = st.sidebar.slider(
    "Previous malaria infections",
    0, 10, 0
)

# Clinical Symptoms
st.sidebar.header("🩺 Clinical Symptoms")

days_of_fever = st.sidebar.slider(
    "Days of fever",
    0, 10, 0
)

has_headache = st.sidebar.checkbox("Headache")
has_chills = st.sidebar.checkbox("Chills/Rigors")
has_fatigue = st.sidebar.checkbox("Fatigue/Weakness")
has_vomiting = st.sidebar.checkbox("Vomiting/Nausea")
appetite_loss = st.sidebar.checkbox("Loss of appetite")

# Lab Results
st.sidebar.header("🔬 Laboratory Results")

rbc_count = st.sidebar.number_input(
    "Red Blood Cell Count (million/µL)",
    min_value=2.0,
    max_value=7.0,
    value=4.5,
    step=0.1
)

wbc_count = st.sidebar.number_input(
    "White Blood Cell Count (thousand/µL)",
    min_value=2.0,
    max_value=15.0,
    value=7.0,
    step=0.1
)

# Predict button
if st.sidebar.button("🔬 Predict Malaria Risk", type="primary"):
    
    # Prepare input data
    input_data = pd.DataFrame({
        'age': [age],
        'temperature_celsius': [temperature],
        'region': [region],
        'season': [season],
        'lives_near_water': [lives_near_water],
        'uses_mosquito_net': [uses_mosquito_net],
        'previous_malaria_cases': [previous_malaria_cases],
        'days_of_fever': [days_of_fever],
        'has_headache': [1 if has_headache else 0],
        'has_chills': [1 if has_chills else 0],
        'has_fatigue': [1 if has_fatigue else 0],
        'has_vomiting': [1 if has_vomiting else 0],
        'appetite_loss': [1 if appetite_loss else 0],
        'red_blood_cell_count': [rbc_count],
        'white_blood_cell_count': [wbc_count]
    })
    
    # Make prediction
    prediction = predict_model(model, data=input_data)
    
    # Display results
    st.markdown("---")
    
    # Patient summary
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Age", f"{age} years")
    with col2:
        temp_status = "🔥 Fever" if temperature > 37.5 else "✅ Normal"
        st.metric("Temperature", f"{temperature}°C", temp_status)
    with col3:
        st.metric("Days of Fever", days_of_fever)
    with col4:
        st.metric("Previous Cases", previous_malaria_cases)
    
    # Prediction result
    predicted_malaria = prediction['prediction_label'].values[0]
    prediction_prob = prediction['prediction_score'].values[0]
    
    st.markdown("### 🎯 Prediction Result")
    
    if predicted_malaria == 1:
        st.markdown(f"""
            <div class="positive-result">
                <h2 style="color: #D32F2F; margin: 0;">⚠️ MALARIA POSITIVE (High Risk)</h2>
                <p style="font-size: 1.3rem; margin: 1rem 0;">
                    Confidence: <strong>{prediction_prob:.1%}</strong>
                </p>
                <hr style="border-color: #D32F2F;">
                <h3>📋 Recommended Actions:</h3>
                <ul style="font-size: 1.05rem;">
                    <li>✅ Perform confirmatory test (RDT or microscopy)</li>
                    <li>💊 If confirmed, start antimalarial treatment immediately</li>
                    <li>🌡️ Monitor temperature and symptoms closely</li>
                    <li>💧 Ensure adequate hydration</li>
                    <li>🏥 Seek immediate medical attention if symptoms worsen</li>
                </ul>
                <p style="color: #D32F2F; font-weight: bold; margin-top: 1rem;">
                    ⚠️ This is a screening result. Laboratory confirmation is required.
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="negative-result">
                <h2 style="color: #4CAF50; margin: 0;">✅ MALARIA NEGATIVE (Low Risk)</h2>
                <p style="font-size: 1.3rem; margin: 1rem 0;">
                    Confidence: <strong>{prediction_prob:.1%}</strong>
                </p>
                <hr style="border-color: #4CAF50;">
                <h3>📋 Recommendations:</h3>
                <ul style="font-size: 1.05rem;">
                    <li>✅ Low malaria risk, but continue monitoring symptoms</li>
                    <li>🦟 Continue using mosquito net</li>
                    <li>💧 Stay hydrated and rest</li>
                    <li>🏥 Consult a doctor if symptoms persist or worsen</li>
                    <li>🔬 Consider testing for other tropical diseases if fever continues</li>
                </ul>
                <p style="color: #4CAF50; font-weight: bold; margin-top: 1rem;">
                    ℹ️ A negative prediction doesn't rule out malaria entirely. Clinical judgment is essential.
                </p>
            </div>
        """, unsafe_allow_html=True)
    
    # Risk factors summary
    st.markdown("### 📊 Risk Factor Analysis")
    
    risk_factors = []
    protective_factors = []
    
    if temperature > 38.0:
        risk_factors.append(f"High fever ({temperature}°C)")
    if days_of_fever > 3:
        risk_factors.append(f"Prolonged fever ({days_of_fever} days)")
    if previous_malaria_cases > 2:
        risk_factors.append(f"Multiple previous infections ({previous_malaria_cases})")
    if lives_near_water == 1:
        risk_factors.append("Lives near water bodies")
    if season == 'Rainy_Season':
        risk_factors.append("Rainy season (high transmission)")
    if rbc_count < 4.0:
        risk_factors.append(f"Low RBC count ({rbc_count})")
    
    if uses_mosquito_net == 1:
        protective_factors.append("Uses mosquito net")
    if temperature < 37.5:
        protective_factors.append("Normal temperature")
    if rbc_count >= 4.5:
        protective_factors.append("Healthy RBC count")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔴 Risk Factors:**")
        if risk_factors:
            for factor in risk_factors:
                st.markdown(f"- {factor}")
        else:
            st.markdown("- No significant risk factors")
    
    with col2:
        st.markdown("**🟢 Protective Factors:**")
        if protective_factors:
            for factor in protective_factors:
                st.markdown(f"- {factor}")
        else:
            st.markdown("- Few protective factors detected")

else:
    # Show information when no prediction yet
    st.info("👈 Fill in the patient details in the sidebar and click 'Predict Malaria Risk' to get started!")
    
    # Stats section
    st.markdown("### 📚 About Malaria in Nigeria")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Key Facts:**
        - Nigeria accounts for 27% of global malaria cases
        - 97% of population at risk of malaria
        - Peak transmission during rainy season
        - Children under 5 most vulnerable
        """)
    
    with col2:
        st.markdown("""
        **Prevention:**
        - Sleep under treated mosquito nets
        - Use insect repellent
        - Eliminate stagnant water
        - Take antimalarial prophylaxis when traveling
        """)

# Footer
st.markdown("---")
st.markdown("""
    <p style="text-align: center; color: #666;">
        🏥 Built for Nigerian Healthcare | Blossom Academy Data Science Project
    </p>
""", unsafe_allow_html=True)



