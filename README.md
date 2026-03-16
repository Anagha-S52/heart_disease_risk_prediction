# heart_disease_risk_prediction
Heart Disease Risk Prediction Web Application built using Machine Learning and Flask. The system analyzes clinical parameters such as age, cholesterol, blood pressure, and ECG results to predict heart disease risk and display possible contributing factors. Includes data preprocessing, model training, and a user-friendly web interface.

Heart Disease Risk Prediction Web Application

This project is a Machine Learning-based Heart Disease Risk Prediction System developed using Python, Flask, and Scikit-learn. The application analyzes key clinical parameters such as age, cholesterol level, blood pressure, ECG readings, and exercise-induced angina to estimate the probability of heart disease risk.

The system provides a simple web interface where users can enter health-related information and receive a risk prediction along with possible contributing factors.

Project Overview

The goal of this project is to demonstrate how data analytics and machine learning can be applied to healthcare data to assist in predicting potential heart disease risk.

This project includes:

Exploratory Data Analysis (EDA)

Data preprocessing and feature scaling

Machine Learning model training

Flask web application deployment

User input interface and prediction results

Logging system for tracking application usage

Features

• Machine Learning-based heart disease prediction
• Interactive web interface built with Flask
• User input validation for medical parameters
• Displays prediction probability and risk level
• Shows possible contributing factors based on inputs
• Stores user access details (Name and Email) in an Excel file

Technologies Used

Python

Flask

Scikit-learn

Pandas

NumPy

HTML & CSS

Joblib

Project Structure
heart-disease-ml

app.py
heart_model.pkl
scaler.pkl
users.xlsx

templates
│
├── access.html
├── index.html
└── result.html

static
│
└── bg.jpg
How It Works

The user accesses the system and enters their name and email.

The user is redirected to the prediction page where they input medical parameters.

The trained machine learning model processes the inputs.

The system displays:

Risk probability

Risk category (Low / Moderate / High)

Possible contributing factors.
