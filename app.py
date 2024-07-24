from flask import Flask, request, jsonify, render_template
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from werkzeug.exceptions import BadRequest
import joblib  # Import joblib

app = Flask(__name__)

MODEL_PATH = 'model.joblib'

# Function to create and save the model
def create_and_save_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, MODEL_PATH)  # Use joblib to save the model

# Function to load the model
def load_model():
    try:
        return joblib.load(MODEL_PATH)  # Use joblib to load the model
    except FileNotFoundError:
        create_and_save_model()
        return joblib.load(MODEL_PATH)

# Load the pre-trained model
model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'features' not in data:
            raise BadRequest("Missing 'features' in request")

        features = np.array(data['features'])
        if features.shape != (4,):
            raise BadRequest("Features should be a list of 4 numbers")

        features = features.reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'Flask API is running'}), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
