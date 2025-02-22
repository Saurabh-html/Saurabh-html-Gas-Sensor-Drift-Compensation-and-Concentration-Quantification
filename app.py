from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
app = Flask(__name__)

# Load the trained model
model, preprocessor = joblib.load('trained_model_and_preprocessor.pkl')

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect gas_type and 128 features
        gas_type = int(request.form['gas_type'])
        features = [float(request.form[f'feature_{i}']) for i in range(1, 129)]  # 1-128

        # Create input DataFrame matching training data structure
        input_df = pd.DataFrame([features], columns=[f"{i}" for i in range(1, 129)])
        input_df['gas_type'] = gas_type

        # Preprocess (scale + one-hot encode)
        input_preprocessed = preprocessor.transform(input_df)

        # Predict
        prediction = model.predict(input_preprocessed)[0]
        return render_template('result.html', prediction=round(prediction, 2))
    except Exception as e:
        return jsonify({'error': str(e)}), 400
if __name__ == '__main__':
    app.run(debug=True)
