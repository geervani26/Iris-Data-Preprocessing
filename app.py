from pathlib import Path

import joblib
import pandas as pd

from flask import Flask, jsonify, render_template, request


# Locate the project directory
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "iris_model.joblib"


# Create the Flask application
app = Flask(__name__)


# Load the trained model
model = joblib.load(MODEL_PATH)

print("Iris model loaded successfully!")


# Define the four required input features
FEATURES = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
]


# Display the home page
@app.route("/")
def home():
    return render_template("index.html")


# Create the prediction API
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "error": "Please send a valid JSON object."
            }), 400

        # Check that all required measurements are present
        missing_features = [
            feature for feature in FEATURES
            if feature not in data
        ]

        if missing_features:
            return jsonify({
                "error": "Missing measurements.",
                "missing_features": missing_features
            }), 400

        # Convert the inputs to numbers
        try:
            measurements = {
                feature: float(data[feature])
                for feature in FEATURES
            }
        except (TypeError, ValueError):
            return jsonify({
                "error": "All measurements must be numbers."
            }), 400

        # Check for invalid numeric values
        import math

        if not all(
            math.isfinite(value)
            for value in measurements.values()
        ):
            return jsonify({
                "error": "Measurements must be finite numbers."
            }), 400

        # Check that measurements are positive
        if not all(
            value > 0
            for value in measurements.values()
        ):
            return jsonify({
                "error": "Measurements must be greater than zero."
            }), 400

        # Prepare input in the format expected by the model
        input_data = pd.DataFrame(
            [measurements],
            columns=FEATURES
        )

        # Predict the flower species
        prediction = model.predict(input_data)[0]

        return jsonify({
            "predicted_species": str(prediction),
            "input_measurements": measurements
        })

    except Exception:
        app.logger.exception("Prediction failed")

        return jsonify({
            "error": "Prediction failed. Please check the server logs."
        }), 500


# Start the Flask development server
if __name__ == "__main__":
    app.run(debug=True)