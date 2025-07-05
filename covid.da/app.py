from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and encoders
model = pickle.load(open('model.pkl', 'rb'))
encoders = pickle.load(open('encoders.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form = request.form
        input_data = {
            'Age': int(form['age']),
            'Gender': encoders['Gender'].transform([form['gender']])[0],
            'Vaccine_Type': encoders['Vaccine_Type'].transform([form['vaccine_type']])[0],
            'Doses_Taken': int(form['doses']),
            'Booster_Taken': encoders['Booster_Taken'].transform([form['booster']])[0],
            'Diabetes': encoders['Diabetes'].transform([form['diabetes']])[0],
            'Hypertension': encoders['Hypertension'].transform([form['hypertension']])[0],
            'Immune_Score': encoders['Immune_Score'].transform([form['immune_score']])[0],
        }

        df = pd.DataFrame([input_data])
        prediction = model.predict(df)[0]
        prediction_label = encoders['Reinfection'].inverse_transform([prediction])[0]

        # Map prediction to risk image
        risk_images = {
            "Low": "low-risk.png",
            "Medium": "medium-risk.png",
            "High": "high-risk.png"
        }
        image_file = risk_images.get(prediction_label, "default.png")

        return render_template('result.html', prediction=prediction_label, risk_image=image_file)
    
    except Exception as e:
        print(f"Error: {e}")
        return render_template('result.html', prediction="Error: Invalid input", risk_image="default.png")

if __name__ == '__main__':
    app.run(debug=True)
