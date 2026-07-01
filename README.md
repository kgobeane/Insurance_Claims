# 🛡️ Insurance Fraud Detection using Machine Learning

## 📌 Project Overview

Insurance fraud is a significant challenge for insurance companies, resulting in billions of dollars in financial losses each year. Detecting fraudulent claims early enables insurers to reduce financial risk, improve operational efficiency, and ensure legitimate customers receive timely claim settlements.

This project presents an end-to-end insurance fraud detection solution by combining **SQL Server** for data cleaning and preparation, **Python** for exploratory data analysis and machine learning, **Streamlit** for deploying an interactive prediction application, and **Power BI** for executive reporting and business intelligence dashboards.

The solution predicts whether an insurance claim is **Fraudulent** or **Legitimate** based on customer and claim-related information while providing actionable insights through interactive dashboards.

---
<img width="1918" height="798" alt="image" src="https://github.com/user-attachments/assets/22ebeb10-1d3f-40a7-9c42-7ade582e3168" />
<img width="1282" height="722" alt="image" src="https://github.com/user-attachments/assets/7ecb371f-724f-40c7-95fa-c3f1d0e45481" />
<img width="1283" height="730" alt="image" src="https://github.com/user-attachments/assets/854b1bed-5dbe-460f-9d8d-f1e8db789c21" />
<img width="1282" height="725" alt="image" src="https://github.com/user-attachments/assets/32d92b66-9ca4-45f5-a56a-30e179137356" />





# 🎯 Business Problem

Insurance companies process thousands of claims every Month, making manual fraud detection time-consuming, costly, and prone to human error. The objective of this project is to build a machine learning solution that identifies potentially fraudulent claims before approval, allowing investigators to focus on high-risk cases while improving the efficiency of legitimate claim processing.

---

# 🎯 Project Objectives

- Clean and prepare insurance claims data using SQL Server.
- Perform Exploratory Data Analysis (EDA) in Python.
- Engineer relevant features for machine learning.
- Handle class imbalance using SMOTE.
- Train and compare multiple machine learning classification models.
- Optimize and evaluate the best-performing model.
- Deploy the final model using Streamlit.
- Build an interactive Power BI dashboard for business reporting.

---

# 🔄 Project Workflow

1. Data Cleaning using SQL Server
2. Data Import into Python
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Data Preprocessing
6. Feature Scaling
7. Train-Test Split
8. Handling Class Imbalance using SMOTE
9. Machine Learning Model Development
10. Hyperparameter Tuning
11. Model Evaluation
12. Streamlit Deployment
13. Power BI Dashboard Development

---

# 📂 Dataset

The dataset contains historical insurance claim records, including customer demographics, policy information, premiums, claim amounts, claim status, and fraud indicators.

### Features Used for Machine Learning

- Age
- Monthly Income
- Premium Amount
- Claim Amount

### Target Variable

- Legitimate Claim (0)
- Fraudulent Claim (1)

---

# 🛠️ Technologies Used

### Database

- SQL Server (T-SQL)

### Programming

- Python

### Python Libraries

- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Matplotlib
- Joblib

### Machine Learning

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

### Deployment

- Streamlit

### Business Intelligence

- Power BI

### Version Control

- Git
- GitHub

---

# 🧹 Data Cleaning and Preparation

## SQL Server

The raw insurance claims dataset was cleaned using SQL Server before being imported into Python.

The SQL cleaning process included:

- Data quality assessment
- Duplicate identification and removal
- Missing value analysis
- Data validation
- Standardization of data formats
- Preparing a clean analytical dataset for machine learning

## Python

After SQL cleaning, Python was used to:

- Import the cleaned dataset
- Perform feature selection
- Scale numerical features using StandardScaler
- Split data into training and testing datasets
- Balance the dataset using SMOTE
- Prepare the final dataset for machine learning

---

# 📊 Exploratory Data Analysis (EDA)

EDA was conducted to better understand customer behaviour and claim characteristics.

The analysis included:

- Statistical summaries
- Distribution of claim amounts
- Fraud distribution
- Age group analysis
- Policy type analysis
- Claim status analysis
- Correlation analysis
- Outlier detection

---

# 🤖 Machine Learning

The following classification algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

After comparing model performance, **Gradient Boosting** was selected as the final production model due to its superior balance between predictive performance and fraud detection capability.

---

# 📈 Model Evaluation

The final model was evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score
- Classification Report
- Confusion Matrix

Special emphasis was placed on fraud detection metrics, as correctly identifying fraudulent claims is more important than maximizing overall accuracy.

---

# 🌐 Streamlit Application

An interactive Streamlit web application was developed to demonstrate the deployed machine learning model.

Users can:

- Enter customer claim details
- Predict whether a claim is Fraudulent or Legitimate
- View fraud probability
- View risk level
- Receive business recommendations based on prediction results

---

# 📊 Power BI Dashboard

An executive Power BI dashboard was developed to communicate business insights through three interactive pages.

## 1️⃣ Executive Overview

Provides a high-level summary of insurance claims performance.

Key metrics include:

- Total Claims
- Total Claim Amount
- Average Claim Amount
- Approval Rate
- Fraud Rate

Visualizations include:

- Monthly claim trends
- Claim amount by policy type
- Claim status distribution
- Fraud cases by province
- Claims by age group
- Fraud analysis

---

## 2️⃣ Claims Analysis

Provides detailed analysis of customer claims across demographics and policy types.

Visualizations include:

- Claims by policy type
- Claims by age group
- Claims by gender
- Average claim amount by age group
- Policy performance table

---

## 3️⃣ Fraud & Risk Analysis

Focuses on fraud trends and operational risk.

Visualizations include:

- Fraud cases by month
- Fraud rate
- Fraud by policy type
- Fraud by age group
- Fraud hotspots by province
- Claims approval and rejection analysis

---

# 💡 Business Recommendations

- Strengthen fraud detection controls for Home, Life, and Auto insurance policies.
- Prioritize investigations for customers within the 36–45 age group, where claim and fraud activity are highest.
- Increase fraud monitoring during months with elevated fraud trends.
- Implement machine learning models to support early fraud detection.
- Use Power BI dashboards for continuous monitoring of claims performance and fraud patterns.

---

# 📁 Project Structure

```text
Insurance_Fraud_Detection/
│
├── data/
│   └── Insurance_Claims.csv
│
├── SQL/
│   └── Data_Cleaning.sql
│
├── notebooks/
│   └── Insurance_Fraud_Detection.ipynb
│
├── models/
│   ├── fraud_model.pkl
│   ├── scaler.pkl
│   └── features.pkl
│
├── dashboard/
│   └── Insurance_Fraud_Dashboard.pbix
│
├── screenshots/
│
├── Insurance_Claims.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Insurance_Fraud_Detection.git
```

Navigate into the project folder:

```bash
cd Insurance_Fraud_Detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run Insurance_Claims.py
```

---

# 📈 Business Value

This project demonstrates how SQL, Machine Learning, and Business Intelligence can be integrated to improve fraud detection in the insurance industry.

The solution helps organizations:

- Detect suspicious claims earlier.
- Reduce financial losses caused by fraud.
- Improve operational efficiency.
- Support faster claim processing.
- Enable data-driven decision-making through interactive dashboards.

---

# 🔮 Future Improvements

Potential enhancements include:

- Real-time fraud prediction using APIs.
- Integration with cloud platforms (Azure/AWS).
- Explainable AI (SHAP/LIME) for model transparency.
- Automated model retraining pipelines.
- Continuous monitoring of model performance.

---

# 👨‍💻 Author

**Kgobeane Mahlo**

Aspiring Data Scientist | Machine Learning Engineer | Business Intelligence Analyst

**Skills:** SQL • Python • Machine Learning • Streamlit • Power BI • Git • GitHub

GitHub: https://github.com/kgobeane
