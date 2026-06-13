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

$env:MLFLOW_TRACKING_PASSWORD="<token>"

# Installation
Clone Repository
```bash
git clone https://github.com/your-username/WineQuality.git
cd WineQuality
```

Create Virtual Environment
```bash
python -m venv env
```

Activate Environment
Windows:
```bash
env\Scripts\activate
```

Linux / Mac:
```bash
source env/bin/activate
```

Install Dependencies
```bash
pip install -r requirements.txt
```
Run Training Pipeline

```bash
python main.py
```


# AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment

```bash
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```

3. Create ECR repo to store/save docker image

```bash
- Save the URI: 970547337635.dkr.ecr.ap-south-1.amazonaws.com/mlproj
```


4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:


```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```
6. Configure EC2 as self-hosted runner:

```bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```
7. Setup github secrets:
```bash

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app
```

Author

Kanishka Bansal

B.Tech Computer Science Engineering

Thapar Institute of Engineering and Technology


