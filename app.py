from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    model = pickle.load(open("CCPP.pkl", "rb"))
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Error loading model:", e)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Prediction Page
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        try:
            AT = float(request.form['AT'])
            V = float(request.form['V'])
            AP = float(request.form['AP'])
            RH = float(request.form['RH'])

            # Convert input into a NumPy array
            input_features = np.array([[AT, V, AP, RH]])

            # Predict output
            prediction = round(model.predict(input_features)[0], 4)
        except Exception as e:
            return f"❌ Error: {e}"

    return render_template('predict.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
