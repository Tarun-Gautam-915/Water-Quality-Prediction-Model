from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the retrained model
model_path = "water_quality_model_v3.pkl"
model = joblib.load(model_path)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/survey', methods=["GET", "POST"])
def survey():
    prediction = None
    if request.method == "POST":
        features = [float(request.form.get(param)) for param in [
            "ph", "sulfate", "chloramines", "hardness", "conductivity", "organic_carbon", "turbidity"]]
        prediction_value = model.predict([features])[0]
        prediction = "Safe" if prediction_value == 1 else "Not Safe"
    
    return render_template('survey.html', prediction=prediction)

@app.route('/tds', methods=["GET", "POST"])
def tds():
    result = None
    tds_value = None
    if request.method == "POST":
        try:
            tds_value = float(request.form.get("tds"))
            if tds_value <= 150:
                result = f"TDS Value: {tds_value} - Excellent Quality for drinking"
            elif 150 < tds_value <= 300:
                result = f"TDS Value: {tds_value} - Good Quality for drinking"
            elif 300 < tds_value <= 500:
                result = f"TDS Value: {tds_value} - Fair Quality for drinking, taste differs"
            elif 500 < tds_value <= 1000:
                result = f"TDS Value: {tds_value} - Poor Quality for drinking"
            else:
                result = f"TDS Value: {tds_value} - Unacceptable for drinking"
        except ValueError:
            result = "Invalid input! Please enter a numeric value."

    return render_template('tds.html', result=result, tds_value=tds_value)

@app.route('/ph', methods=["GET", "POST"])
def ph():
    result = None
    ph_value = None

    if request.method == "POST":
        try:
            ph_value = float(request.form.get("ph"))
            if ph_value < 6.5:
                result = f"pH Value: {ph_value} - Acidic, not suitable for drinking. 🚫"
            elif 6.5 <= ph_value <= 8.5:
                result = f"pH Value: {ph_value} - Neutral, suitable for drinking. ✅"
            else:
                result = f"pH Value: {ph_value} - Alkaline, may not be ideal for drinking. ⚠️"
        except ValueError:
            result = "Invalid input! Please enter a numeric value."

    return render_template('ph.html', result=result, ph_value=ph_value)


if __name__ == "__main__":
    app.run(debug=True)
