from flask import Blueprint, render_template, request
import joblib
import numpy as np

main = Blueprint('main', __name__)

# Load your Random Forest model
model = joblib.load('models/best_model.pkl')

# List of expected input features in the correct order:
FEATURES = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
    'restecg', 'thalach', 'exang', 'oldpeak', 'slope',
    'ca', 'thal'
]

@main.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
            # Get input values from the form, convert to float
            input_data = [float(request.form.get(feat)) for feat in FEATURES]

            # Reshape and predict
            input_array = np.array(input_data).reshape(1, -1)
            pred = model.predict(input_array)[0]
            prediction = 'Heart Disease Present' if pred == 1 else 'No Heart Disease'

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('index.html', prediction=prediction)
