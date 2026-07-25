from pydantic import BaseModel, Field
from typing import Dict


class PredictionResponse(BaseModel):

    predicted_category: str = Field(
        ..., 
        description="Predicted insurance category", 
        example="High"
    )
    confidence: float = Field(
        ..., 
        description="Confidence score of the prediction", 
        example=0.85
    )
