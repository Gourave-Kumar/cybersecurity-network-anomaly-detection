# SafeX Cybersecurity Network Anomaly Detection

A machine learning project for detecting **normal network traffic** and **attack/anomalous network traffic** using the **UNSW-NB15 cybersecurity dataset**.  
This project includes a complete ML pipeline and a simple **Streamlit prototype** for interactive prediction.

---

## Project Overview

Cybersecurity teams need systems that can identify suspicious traffic patterns before they cause serious damage. This project builds a predictive model that analyzes network-flow features and classifies traffic as either:

- **0 = Normal Traffic**
- **1 = Attack / Anomaly**

The project goes beyond basic EDA and includes data cleaning, feature engineering, model training, model comparison, hyperparameter tuning, evaluation, visualization, model saving, and a Streamlit web app prototype.

---

## Objective

The objective of this project is to build an end-to-end machine learning pipeline for cybersecurity network-anomaly detection.

The final system can:

- Load and explore the UNSW-NB15 dataset
- Clean and preprocess network traffic data
- Create new engineered features
- Train and compare multiple ML models
- Tune the best model
- Evaluate model performance using classification metrics
- Visualize model results
- Predict normal vs anomalous traffic through a Streamlit app

---

## Dataset

**Dataset:** UNSW-NB15 Network Intrusion Detection Dataset

The dataset contains network traffic records with features such as:

- Protocol
- Service
- Connection state
- Duration
- Source bytes
- Destination bytes
- Source packets
- Destination packets
- Attack category
- Binary label

For this project, the `label` column is used as the target variable.

The `attack_cat` column is removed from input features because it directly describes the attack category and could cause data leakage.

---

## Target Variable

| Label | Meaning |
|---|---|
| 0 | Normal Traffic |
| 1 | Attack / Anomaly |

---

## Project Workflow

1. Import required libraries
2. Load training and testing datasets
3. Explore dataset shape, data types, and target distribution
4. Check missing values and duplicate records
5. Clean the data
6. Engineer new cybersecurity-related features
7. Convert categorical columns to correct data types
8. Separate input features and target variable
9. Remove data leakage column
10. Align train and test columns
11. Apply preprocessing using sklearn pipelines
12. Train Logistic Regression
13. Train Random Forest Classifier
14. Train Extra Trees Classifier
15. Compare model performance
16. Tune the best model using RandomizedSearchCV
17. Evaluate the tuned model
18. Create confusion matrix
19. Create ROC curve
20. Analyze feature importance
21. Save trained model and outputs
22. Build Streamlit prototype

---

## Feature Engineering

The following new features were created to improve prediction quality:

### 1. Total Bytes

Total transferred data in a network flow.

```python
total_bytes = sbytes + dbytes
```

### 2. Total Packets

Total packets exchanged between source and destination.

```python
total_packets = spkts + dpkts
```

### 3. Bytes Per Second

Traffic throughput or speed of data transfer.

```python
bytes_per_second = total_bytes / duration
```

### 4. Average Packet Size

Average size of packets in the network flow.

```python
avg_packet_size = total_bytes / total_packets
```

### 5. Byte Ratio

Ratio between source bytes and destination bytes.

```python
byte_ratio = sbytes / dbytes
```

These features help the model understand traffic intensity, packet behavior, and unusual source-to-destination communication patterns.

---

## Machine Learning Models

Three models were trained and compared:

1. **Logistic Regression**
2. **Random Forest Classifier**
3. **Extra Trees Classifier**

The best-performing model in this project was:

```text
Tuned Extra Trees Classifier
```

---

## Evaluation Metrics

The following metrics were used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

In cybersecurity anomaly detection, **Recall** is especially important because a false negative means an actual attack was classified as normal traffic.

---

## Final Model Performance

> Replace these values with the actual results from your notebook output.

| Metric | Score |
|---|---:|
| Accuracy | Add your value |
| Precision | Add your value |
| Recall | Add your value |
| F1 Score | Add your value |
| ROC-AUC | Add your value |

---

## Visualizations

The project generates the following visualizations:

### Confusion Matrix

Shows how many normal and attack records were correctly or incorrectly classified.

```text
images/confusion_matrix.png
```

### ROC Curve

Shows how well the model separates normal traffic from attack traffic.

```text
images/roc_curve.png
```

### Feature Importance

Shows which features contributed most to model predictions.

```text
images/feature_importance.png
```

---

## Key Findings

The Extra Trees Classifier performed best compared to Logistic Regression and Random Forest. The model was able to classify normal and anomalous network traffic using flow-based network features. Engineered features such as total bytes, total packets, bytes per second, average packet size, and byte ratio helped improve the model's understanding of traffic behavior. Feature importance analysis helped identify which network characteristics were most useful for anomaly detection. In cybersecurity, reducing false negatives is important because missed attacks can create serious security risks.

---

## Streamlit Prototype

A simple Streamlit app was created to demonstrate the trained model.

The user can enter network traffic values such as:

- Protocol
- Service
- Connection state
- Duration
- Source bytes
- Destination bytes
- Source packets
- Destination packets

The app then predicts:

```text
Normal Network Traffic
```

or

```text
Attack / Anomaly Detected
```

The Streamlit app also includes the SafeX company logo in the interface.

---

## Project Structure

```text
Week4_Cybersecurity_Anomaly_Detection/
│
├── cybersecurity_network_anomaly_detection.ipynb
├── app.py
├── README.md
├── requirements.txt
│
├── Week4 Task/
│   └── safexsolutions_logo.jpg
│
├── data/
│   ├── UNSW_NB15_training-set.parquet
│   └── UNSW_NB15_testing-set.parquet
│
├── model/
│   ├── cybersecurity_anomaly_detector.pkl
│   ├── feature_columns.pkl
│   └── categorical_columns.pkl
│
├── images/
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   └── feature_importance.png
│
└── outputs/
    ├── final_model_metrics.csv
    ├── model_comparison.csv
    └── feature_importance.csv
```

---

## Installation

Install the required libraries:

```bash
pip install pandas numpy scikit-learn matplotlib streamlit joblib pyarrow
```

Or install using `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## How to Run the Notebook

Open Jupyter Notebook and run:

```text
cybersecurity_network_anomaly_detection.ipynb
```

Run the notebook cells from top to bottom.

The notebook will generate:

- Trained model
- Final metrics
- Model comparison table
- Feature importance file
- Confusion matrix image
- ROC curve image
- Feature importance image

---

## How to Run the Streamlit App

Run this command from the project folder:

```bash
streamlit run app.py
```

After running the command, the app will open in the browser at:

```text
http://localhost:8501
```

---

## Technologies Used

- Python
- pandas
- numpy
- scikit-learn
- matplotlib
- Jupyter Notebook
- Streamlit
- joblib
- pyarrow

---

## Future Improvements

Future improvements can include:

- Using live network traffic from Wireshark/PCAP files
- Adding more advanced models such as XGBoost or LightGBM
- Improving feature engineering with flow-level cybersecurity features
- Deploying the Streamlit app online
- Adding a dashboard for batch predictions
- Adding model explainability using SHAP

---

## Conclusion

This project demonstrates a complete machine learning workflow for cybersecurity network anomaly detection. It includes data exploration, cleaning, feature engineering, model comparison, hyperparameter tuning, evaluation, visualizations, and a Streamlit prototype.

The final prototype works as a basic ML-powered intrusion detection demo that predicts whether network traffic is normal or suspicious.
