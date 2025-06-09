# Heart Disease Prediction Web App

A web application built with Flask that predicts heart disease using machine learning.

![Heart Attack Prediction](defining-heart-attack.jpg)

## Features

- Web interface for heart disease prediction
- Random Forest model for accurate predictions
- Bootstrap 5 responsive design
- Deployed on Render cloud platform

## Prerequisites

- Python 3.10+
- pip package manager

## Installation

1. Clone the repository:
```sh
git clone https://github.com/kavyaatn/heart_attack_detection.git
cd heart-attack
```

2. Create and activate virtual environment:
```sh
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

1. Start the Flask development server:
```sh
flask run
```

2. Open `http://localhost:5000` in your browser

3. Enter the required medical parameters:
   - Age
   - Sex
   - Chest Pain Type (CP)
   - Resting Blood Pressure
   - Cholesterol
   - Fasting Blood Sugar
   - Rest ECG
   - Maximum Heart Rate
   - Exercise Induced Angina
   - ST Depression
   - ST Slope
   - Number of Major Vessels
   - Thalassemia

4. Click "Predict" to see the results

## Deployment on Render

This application is configured for deployment on Render using the [`render.yaml`](render.yaml) configuration:

1. Create a new account on [Render](https://render.com)

2. Connect your GitHub repository

3. Render will automatically detect the configuration and deploy the app

4. The application will be available at `https://heart-disease-predictor.onrender.com`

## Project Structure

```
├── app/
│   ├── __init__.py
│   └── routes.py
├── models/
│   └── best_model.pkl
├── templates/
│   └── index.html
├── requirements.txt
└── render.yaml
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request