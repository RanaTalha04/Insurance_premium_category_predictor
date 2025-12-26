# 🩺 Insurance Premium Category Prediction

A machine learning–powered FastAPI application that predicts insurance premium categories (Low / Medium / High) based on user input features. The project is fully Dockerized for easy deployment and reproducibility.

---

## 🎯 Objectives
- Predict insurance premium category using ML
- Provide predictions via RESTful API
- Ensure reproducible deployment using Docker
- Follow clean ML + backend separation

---

## 🧠 Machine Learning Pipeline

- Data preprocessing
- Feature transformation
- Model training using scikit-learn
- Model saved as a serialized pipeline (pipe.pkl)
- Loaded at runtime for inference

---

## 🚀 Features

- ML-based insurance premium classification
- REST API built using FastAPI
- Pre-trained scikit-learn pipeline
- Docker support for production-ready deployment
- Swagger UI for API testing

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **ML Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Streamlit, Joblib Docker
- **Tools:** Jupyter Notebook
- **IDE:** VS Code
- **Backend:** FastAPI, Uvicorn
- **DevOps:** Docker

--- 

## 📂 Project Structure

1. The project structure I have:

   ```bash

    Insurance-Premium-Category/
    │
    ├── venv/
    |
    ├── Model/
    │   ├── predict.py              # prediction file
    │   ├── model.pkl               # Trained Model
    |
    ├── data/
    |   ├── insurance             # raw data file
    |
    ├── Backend/ 
    │   ├── config/               # Config folder
    │       ├── city_tiers.py     # City Tier File
    │   ├── Schema/               # Schema folder
    │       ├── prediction_response.py     # Prediction Response File
    │       ├── user_input.py     # User Input File
    │   ├── app.py              # Application
    │   ├── __init__.py
    |
    ├── Frontend/ 
    │   ├── frontend.py              # Frontend
    │
    ├── .gitignore             # git ignore file
    ├── EDA Notebook             # Notebook
    ├── model.pkl                # Trained Model 
    ├── requirements.txt         # Runtime dependencies
    ├── Dockerfile               # Docker configuration
    └── README.md
    
---

## 🚀 API Usage

1. Endpoint:
   ```bash
   POST /predict
   
2. Sample Request:
   ```bash
    {
    "age": 35,
    "income": 75000,
    "dependents": 2,
    "health_score": 7
    }
   
3. Sample Response:
    ```bash
    {
    "predicted_category": "High",
    "confidence": 0.87
    }

---

## 🐳 Docker Deployment

1. Build Image:
   ```bash
   docker build -t insurance-premium .
   
2. Run Container:
   ```bash
    docker run -p 8000:8000 insurance-premium

   
3. Access API:
    ```bash
    http://localhost:8000/docs

--- 

## ✅ Key Highlights

- End-to-end ML deployment
- Production-ready FastAPI backend
- Clean Docker setup
- Version-pinned dependencies

--- 

## 📘 Future Improvements

- Add input validation & logging
- Add CI/CD pipeline
- Model monitoring & retraining

## 👨‍💻 Author
**Muhammad Talha**  
Final-year Computer Science student at UET Lahore  

📫 [Email](mailto:muhammadtalhashahid2005@gmail.com)  
🌐 [Portfolio](https://talhashahid.netlify.app)  
💼 [LinkedIn](https://www.linkedin.com/in/muhammadtaalhaa/)  
💻 [GitHub](https://github.com/RanaTalha04)
