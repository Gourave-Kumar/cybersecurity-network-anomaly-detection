import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# ==========================================
# LOAD MODEL AND FEATURES
# ==========================================

model = joblib.load(
    "model/cybersecurity_anomaly_detector.pkl"
)

feature_columns = joblib.load(
    "model/feature_columns.pkl"
)


# ==========================================
# FEATURE ENGINEERING FUNCTION
# ==========================================

def engineer_features(df):
    df = df.copy()

    if "sbytes" in df.columns and "dbytes" in df.columns:
        df["total_bytes"] = df["sbytes"] + df["dbytes"]

    if "spkts" in df.columns and "dpkts" in df.columns:
        df["total_packets"] = df["spkts"] + df["dpkts"]

    if "total_bytes" in df.columns and "dur" in df.columns:
        df["bytes_per_second"] = (
            df["total_bytes"] / (df["dur"] + 0.000001)
        )

    if "total_bytes" in df.columns and "total_packets" in df.columns:
        df["avg_packet_size"] = (
            df["total_bytes"] / (df["total_packets"] + 1)
        )

    if "sbytes" in df.columns and "dbytes" in df.columns:
        df["byte_ratio"] = (
            df["sbytes"] / (df["dbytes"] + 1)
        )

    return df

LOGO_PATH = r"D:\Week4_Cybersecurity_Anomaly_Detection\safexsolutions_logo.jfif"

# ==========================================
# STREAMLIT UI
# ==========================================

st.set_page_config(
    page_title="SafeX Cybersecurity Anomaly Detector",
    page_icon="🛡️",
    layout="wide"
)

# Company Logo
if os.path.exists(LOGO_PATH):
    col1, col2 = st.columns([1, 5])

    with col1:
        st.image(
            LOGO_PATH,
            width=120
        )

    with col2:
        st.title("SafeX Cybersecurity Anomaly Detection")
        st.write(
            "Machine Learning based prototype for detecting normal and anomalous network traffic."
        )
else:
    st.title("SafeX Cybersecurity Anomaly Detection")
    st.write(
        "Machine Learning based prototype for detecting normal and anomalous network traffic."
    )

st.markdown("---")

st.sidebar.header("Enter Network Traffic Values")

# Sidebar Logo
if os.path.exists(LOGO_PATH):
    st.sidebar.image(
        LOGO_PATH,
        width=50
    )


# ==========================================
# USER INPUTS
# ==========================================

proto = st.sidebar.selectbox(
    "Protocol",
    ["tcp", "udp", "icmp"]
)

service = st.sidebar.selectbox(
    "Service",
    ["-", "http", "ftp", "smtp", "dns", "ssh"]
)

state = st.sidebar.selectbox(
    "Connection State",
    ["FIN", "CON", "INT", "REQ", "RST"]
)

dur = st.sidebar.number_input(
    "Duration",
    min_value=0.0,
    value=1.0
)

sbytes = st.sidebar.number_input(
    "Source Bytes",
    min_value=0,
    value=500
)

dbytes = st.sidebar.number_input(
    "Destination Bytes",
    min_value=0,
    value=300
)

spkts = st.sidebar.number_input(
    "Source Packets",
    min_value=0,
    value=10
)

dpkts = st.sidebar.number_input(
    "Destination Packets",
    min_value=0,
    value=8
)


# ==========================================
# CREATE INPUT DATAFRAME
# ==========================================

input_data = {}

for col in feature_columns:
    input_data[col] = [0]

input_data["proto"] = [proto]
input_data["service"] = [service]
input_data["state"] = [state]

input_data["dur"] = [dur]
input_data["sbytes"] = [sbytes]
input_data["dbytes"] = [dbytes]
input_data["spkts"] = [spkts]
input_data["dpkts"] = [dpkts]

input_df = pd.DataFrame(input_data)

input_df = engineer_features(input_df)

for col in feature_columns:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[feature_columns]


# ==========================================
# PREDICTION
# ==========================================

if st.button("Analyze Network Traffic"):

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Attack / Anomaly Detected")
    else:
        st.success("✅ Normal Network Traffic")

    st.write(f"Attack Probability: **{probability * 100:.2f}%**")

    st.subheader("Input Data Used by Model")
    st.dataframe(input_df)