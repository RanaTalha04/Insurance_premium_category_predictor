from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Backend.Schema.user_input import UserInput
from Model.predict import predict_output, MODEL_VERSION
from Backend.Schema.prediction_response import PredictionResponse

### Initialize FastAPI app
app = FastAPI()

### Define API endpoint for prediction


@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API"}


@app.get("/health")
def health_check():
    return {
        "status": "API is healthy and running",
        "model_loaded": "Model loaded successfully",
        "model_version": MODEL_VERSION,
    }


@app.post("/predict", response_model=PredictionResponse)
def predict_insurance(data: UserInput):
    input = {
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "income_lpa": data.income_lpa,
        "city_tier": data.city_tier,
        "occupation": data.occupation,
    }

    try:
        prediction = predict_output(user_input=input)

        ### Return prediction as JSON response
        return JSONResponse(status_code=200, content={"predicted_category": prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
