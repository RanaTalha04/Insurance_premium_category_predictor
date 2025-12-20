import pandas as pd
import pickle
import os

### Load the pre-trained model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../Model", "model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


### Model Version

MODEL_VERSION = "1.0.0"

class_labels = model.classes_.tolist()


def predict_output(user_input: pd.DataFrame) -> str:
    """
    Predict the insurance premium category based on user input.

    Args:
        user_input (pd.DataFrame): DataFrame containing user input features.

    Returns:
        str: Predicted insurance premium category.
    """
    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)[0]

    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)

    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": prediction,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs,
    }
