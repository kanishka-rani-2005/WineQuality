# Wine Quality Prediction

An End-to-End Machine Learning Project built using Python, Flask, Scikit-Learn, DVC, MLflow, Docker, and CI/CD.

This application predicts the quality of red wine based on its physicochemical properties using an ElasticNet Regression model.

# Project Overview

The goal of this project is to build a complete MLOps pipeline that includes:

Data Ingestion
Data Validation
Data Transformation
Model Training
Model Evaluation
Experiment Tracking with MLflow
Version Control with DVC
Web Application using Flask
Docker Containerization
CI/CD Deployment using GitHub Actions


# MLflow Tracking

Set MLflow Tracking URI:

Windows PowerShell
$env:MLFLOW_TRACKING_URI="https://dagshub.com/<username>/WineQuality.mlflow"

$env:MLFLOW_TRACKING_USERNAME="<username>"

$env:MLFLOW_TRACKING_PASSWORD="YOUR_DAGSHUB_TOKEN"




277426080152.dkr.ecr.us-east-1.amazonaws.com/winequalityproject