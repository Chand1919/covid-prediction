# 🦠 COVID Reinfection Predictor App

A Flask web application that predicts a person's risk of COVID-19 reinfection based on their age, vaccination status, comorbidities, and immune score using a Machine Learning model.

---

## 🚀 Features
- ✅ Predict COVID-19 reinfection risk (*Low*, *Medium*, *High*) based on user inputs
- ✅ User-friendly web interface with HTML, CSS, and JavaScript
- ✅ Dynamic result page showing the prediction and a risk-level image
- ✅ Machine Learning backend (Random Forest Classifier)
- ✅ Ready-to-deploy Flask application

---

## 📂 Folder Structure
covid_reinfection_app/
│
├── app.py # Flask web app
├── train_model.py # ML model training script
├── covid_reinfection_dataset.csv # Dataset for training
├── model.pkl # Trained ML model
├── encoders.pkl # Encoders for categorical variables
│
├── static/
│ ├── css/
│ │ └── style.css
│ ├── js/
│ │ └── script.js
│ └── images/
│ ├── low-risk.png
│ ├── medium-risk.png
│ └── high-risk.png
│
└── templates/
├── index.html # Input form
└── result.html # Prediction result page

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/chand1919/covid-reinfection-predictor.git
cd covid-reinfection-predictor
2️⃣ Install dependencies
Make sure you have Python 3 installed.

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Train the model
bash
Copy
Edit
python train_model.py
This will generate:

✅ model.pkl

✅ encoders.pkl

4️⃣ Run the Flask app
bash
Copy
Edit
python app.py
The app will be available at:
🌐 http://127.0.0.1:5000

🖥️ Screenshots
🔵 Home Page

🔴 Prediction Result

📊 Dataset
This project uses a synthetic dataset covid_reinfection_dataset.csv with the following columns:

Name

Age

Gender

Vaccine_Type

Doses_Taken

Booster_Taken

Diabetes

Hypertension

Immune_Score

Reinfection

You can modify this dataset to add more realistic data.

.

📜 License
This project is licensed under the MIT License.

👩‍💻 Author
chand kumari