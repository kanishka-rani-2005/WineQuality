# 🍷 Wine Quality Prediction

An End-to-End Machine Learning Project built using Flask, Scikit-Learn, MLflow, Docker, and GitHub Actions.

This application predicts the quality of red wine based on its physicochemical properties.

---

## 🚀 Project Overview

This project demonstrates a complete MLOps workflow:

* Data Ingestion
* Data Validation
* Data Transformation
* Model Training
* Model Evaluation
* MLflow Experiment Tracking
* Flask Web Application
* Docker Containerization
* CI/CD using GitHub Actions

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/kanishka-rani-2005/WineQuality.git

cd WineQuality
```

### Create Virtual Environment

Windows:

```bash
python -m venv env

env\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv env

source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Run Training Pipeline

```bash
python main.py
```

This executes:

```text
Data Ingestion
      ↓
Data Validation
      ↓
Data Transformation
      ↓
Model Training
      ↓
Model Evaluation
```

---

## 🌐 Run Web Application

```bash
python app.py
```

Application will be available at:

```text
http://localhost:8080
```

---

## 🐳 Docker Support

### Build Docker Image

```bash
docker build -t winequality .
```

### Run Docker Container

```bash
docker run -p 8080:8080 winequality
```

Visit:

```text
http://localhost:8080
```

---

## 📈 MLflow Tracking

### Windows PowerShell

```powershell
$env:MLFLOW_TRACKING_URI="https://dagshub.com/<username>/WineQuality.mlflow"

$env:MLFLOW_TRACKING_USERNAME="<username>"

$env:MLFLOW_TRACKING_PASSWORD="<token>"
```

### Linux/Mac

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/<username>/WineQuality.mlflow

export MLFLOW_TRACKING_USERNAME=<username>

export MLFLOW_TRACKING_PASSWORD=<token>
```

## 🤖 Model

Algorithm Used:

```python
ElasticNet(
    alpha=0.99,
    l1_ratio=0.8
)
```

### Evaluation Metrics

* RMSE
* MAE
* R² Score

Metrics stored at:

```text
artifacts/model_evaluation/metrics.json
```

---

## 🎯 Input Features

* Fixed Acidity
* Volatile Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Free Sulfur Dioxide
* Total Sulfur Dioxide
* Density
* pH
* Sulphates
* Alcohol

---

---

## 🛠 Tech Stack

### Machine Learning

* Python
* NumPy
* Pandas
* Scikit-Learn

### MLOps

* MLflow
* Dagshub

### Backend

* Flask

### Deployment

* Docker
* GitHub Actions

---

## 🔄 CI/CD

GitHub Actions automatically:

* Installs dependencies
* Runs training pipeline
* Builds Docker image
* Deploys application

---


### Home Page

Users enter wine properties and submit for prediction.

### Prediction Page

Displays predicted wine quality score.

---



# AWS CI/CD Deployment with GitHub Actions

This guide explains how to deploy a Dockerized application to AWS EC2 using GitHub Actions and Amazon ECR.

---

## Architecture

```text
GitHub Repository
        │
        ▼
GitHub Actions
        │
        ▼
Build Docker Image
        │
        ▼
Push Image to Amazon ECR
        │
        ▼
EC2 Self-Hosted Runner
        │
        ▼
Pull Latest Image from ECR
        │
        ▼
Run Docker Container
```

---

# Step 1: Login to AWS Console

1. Open AWS Management Console.
2. Login with your AWS account credentials.
3. Select your preferred AWS Region.

---

# Step 2: Create IAM User for Deployment

Create an IAM user with programmatic access.

## Required Services

### EC2
Used to host and run your application.

### ECR (Elastic Container Registry)
Used to store Docker images.

---

## Deployment Flow

1. Build Docker image from source code.
2. Push Docker image to Amazon ECR.
3. Launch EC2 instance.
4. Pull Docker image from ECR.
5. Run Docker container on EC2.

---

## Required IAM Policies

Attach the following policies to the IAM user:

```text
AmazonEC2ContainerRegistryFullAccess
AmazonEC2FullAccess
```

---

## Create Access Keys

After creating the IAM user:

```text
IAM → Users → Select User → Security Credentials
→ Create Access Key
```

Save:

```text
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
```

---

# Step 3: Create ECR Repository

Navigate to:

```text
AWS Console
→ Elastic Container Registry (ECR)
→ Create Repository
```

Example Repository URI:

```text
970547337635.dkr.ecr.ap-south-1.amazonaws.com/mlproj
```

Save this URI for later use.

---

# Step 4: Launch EC2 Instance

Create an Ubuntu EC2 instance.

Recommended:

```text
AMI: Ubuntu 22.04 LTS
Instance Type: t2.micro (Free Tier)
Storage: 20 GB
```

Security Group:

```text
SSH   : 22
HTTP  : 80
HTTPS : 443
App Port (optional): 5000 / 8000
```

---

# Step 5: Install Docker on EC2

Connect to EC2:

```bash
ssh -i key.pem ubuntu@<EC2_PUBLIC_IP>
```

Update packages:

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
```

Install Docker:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

Verify Docker installation:

```bash
docker --version
```

---

# Step 6: Configure EC2 as GitHub Self-Hosted Runner

Go to:

```text
GitHub Repository
→ Settings
→ Actions
→ Runners
→ New Self-Hosted Runner
```

Select:

```text
Linux
x64
```

Run the commands provided by GitHub on your EC2 machine.

Example:

```bash
mkdir actions-runner && cd actions-runner

curl -o actions-runner-linux-x64.tar.gz -L <runner-url>

tar xzf ./actions-runner-linux-x64.tar.gz

./config.sh --url https://github.com/<username>/<repo> --token <token>

./run.sh
```

---

# Step 7: Configure GitHub Secrets

Navigate to:

```text
GitHub Repository
→ Settings
→ Secrets and Variables
→ Actions
```

Create the following secrets:

```text
AWS_ACCESS_KEY_ID = ****************

AWS_SECRET_ACCESS_KEY = ****************

AWS_REGION = ap-south-1

AWS_ECR_LOGIN_URI = 970547337635.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = mlproj
```

---





## 👨‍💻 Author

**Kanishka Bansal**

B.Tech Computer Science Engineering

Thapar Institute of Engineering and Technology

---

## ⭐ Future Improvements

* Hyperparameter Tuning
* Feature Engineering
* Model Monitoring
* AWS Deployment
* Kubernetes Deployment
* Automated Retraining

---

## 📄 License

This project is licensed under the MIT License.
