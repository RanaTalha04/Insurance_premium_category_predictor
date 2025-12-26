📖 Project Overview

The Insurance Premium Category Prediction System is a machine learning–powered application designed to classify customers into insurance premium categories such as Low, Medium, or High based on personal and financial attributes.

The project focuses on real-world ML deployment, combining model inference with a FastAPI backend and Docker-based containerization, making it production-ready and easily deployable.

🎯 Objectives

Predict insurance premium category using ML

Provide predictions via RESTful API

Ensure reproducible deployment using Docker

Follow clean ML + backend separation

🧠 Machine Learning Pipeline

Data preprocessing

Feature transformation

Model training using scikit-learn

Model saved as a serialized pipeline (pipe.pkl)

Loaded at runtime for inference

⚠️ Note: The scikit-learn version used during training is pinned to avoid pickle compatibility issues.

🏗️ Project Structure
Insurance-Premium-Category/
│
├── Backend/
│   ├── app.py               # FastAPI application
│   ├── pipe.pkl             # Trained ML pipeline
│   ├── __init__.py
│
├── requirements.txt         # Runtime dependencies
├── Dockerfile               # Docker configuration
└── README.md

🛠️ Tech Stack
Backend

FastAPI – high-performance API framework

Uvicorn – ASGI server

Machine Learning

Scikit-learn

NumPy & Pandas

DevOps

Docker – containerized deployment

🚀 API Usage
Endpoint
POST /predict

Sample Request
{
  "age": 35,
  "income": 75000,
  "dependents": 2,
  "health_score": 7
}

Sample Response
{
  "predicted_category": "High",
  "confidence": 0.87
}

🐳 Docker Deployment
Build Image
docker build -t insurance-premium .

Run Container
docker run -p 8000:8000 insurance-premium

Access API
http://localhost:8000/docs


(Swagger UI included 🔥)

✅ Key Highlights

End-to-end ML deployment

Production-ready FastAPI backend

Clean Docker setup

Version-pinned dependencies

Interview & portfolio friendly

🔮 Future Improvements

Add input validation & logging

Add CI/CD pipeline

Model monitoring & retraining

Frontend integration

👨‍💻 Author

Muhammad Talha
Computer Science Student | ML & AI Enthusiast
