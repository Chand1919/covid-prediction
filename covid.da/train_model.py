import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# STEP 1: Load dataset
df = pd.read_csv('covid_reinfection_dataset.csv')

# STEP 2: Drop Name column (not useful for prediction)
df = df.drop('Name', axis=1)

# STEP 3: Encode categorical columns to numeric
label_encoders = {}
for column in df.columns:
    if df[column].dtype == 'object':
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le

# STEP 4: Split dataset
X = df.drop('Reinfection', axis=1)
y = df['Reinfection']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# STEP 5: Train Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# STEP 6: Save trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# STEP 7: Save encoders (for decoding inputs in app.py)
with open('encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)

print("✅ Model trained and saved as model.pkl & encoders.pkl")
