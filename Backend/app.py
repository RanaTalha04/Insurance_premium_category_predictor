from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pandas as pd
import pickle
import os

### Load the pre-trained model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

### Initialize FastAPI app
app = FastAPI()


### Define Pydantic model for input validation

class UserInput(BaseModel):

    age: Annotated[
        int, Field(..., gt=0, lt=120, description="Age of the user in years")
    ]
    weight: Annotated[
        float, Field(..., gt=0, description="Weight of the user in pounds")
    ]
    height: Annotated[
        float, Field(..., gt=0, description="Height of the user in meters")
    ]
    income_lpa: Annotated[
        float, Field(..., gt=0, description="Income of the user in LPA")
    ]
    smoker: Annotated[bool, Field(..., description="Is the user smokes or not?")]
    city: Annotated[str, Field(..., description="City where the user resides")]
    occupation: Annotated[
        Literal[
            "retired",
            "freelancer",
            "student",
            "government_job",
            "business_owner",
            "unemployed",
            "private_job",
        ],
        Field(..., description="Occupation of the user"),
    ]

    ### Computed fields
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return 'High Risk'
        elif self.smoker or self.bmi > 27:
            return 'Moderate Risk'
        else:
            return 'Low Risk'
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'Young'
        elif self.age < 45:
            return 'Adult'
        elif self.age < 60:
            return 'Middle_Aged'
        else:
            return 'Senior'
    
    @computed_field
    @property
    def city_tier(self) -> int:
        tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
        tier_2_cities = [
            "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
            "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
            "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
            "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
            "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
            "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
        ]
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        
### Define API endpoint for prediction
        
@app.post('/predict')
def predict_insurance(data: UserInput):
    input = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group, 
        'lifestyle_risk': data.lifestyle_risk,
        'income_lpa': data.income_lpa,
        'city_tier': data.city_tier, 
        'occupation': data.occupation
    }])
    
    prediction = model.predict(input)[0]
    
    ### Return prediction as JSON response
    return JSONResponse(status_code=200, content={'predicted_category': prediction})