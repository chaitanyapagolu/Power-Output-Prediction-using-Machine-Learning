🔌 Power Output Prediction using Machine Learning
📌 Project Overview
This project predicts the full load electrical power output of a Combined Cycle Power Plant (CCPP) using Machine Learning. By analyzing environmental factors like temperature, exhaust vacuum, pressure, and humidity, the model estimates power output in megawatts (MW).

The project includes a Flask-based web application that allows users to input values and get real-time predictions.

🛠️ Technologies Used
Programming Language: Python
Machine Learning: Scikit-Learn (Random Forest Regressor)
Web Framework: Flask
Frontend: HTML, CSS
Data Visualization: Matplotlib, Seaborn.


📂 Project Structure
graphql
Copy
Edit
CCPP_Prediction/
│── app.py                  # Flask backend application
│── train_model.py           # Model training script
│── CCPP.pkl                 # Saved Machine Learning model
│── dataset.csv              # Power Plant Dataset
│── templates/               # HTML files for UI
│   │── home.html            # Home Page
│   │── index.html           # Prediction Page
│── static/                  # CSS and images
│   │── main.css             # Styling for UI
│   │── background.jpg       # Background image
│── README.md                # Project documentation



📥 Installation & Setup
1️⃣ Install Required Libraries
Run the following command to install dependencies:

pip install flask numpy pandas scikit-learn matplotlib seaborn pickle5
2️⃣ Run the Flask Application
Start the web server by running:
python app.py
After running the command, open your browser and visit:
http://127.0.0.1:5000/
📊 How to Use the Application
1️⃣ Open http://127.0.0.1:5000/ in a web browser.
2️⃣ Enter input values for:

AT (Ambient Temperature in °C)
V (Exhaust Vacuum in cm Hg)
AP (Ambient Pressure in mbar)
RH (Relative Humidity in %)
3️⃣ Click Predict to get the power output estimate.
📌 Sample Inputs & Expected Outputs
AT (°C)	V (cm Hg)	AP (mbar)	RH (%)	Predicted Power Output (MW)
20.5	50.2	1010.3	60.5	455.01 MW
25.0	40.0	1005.0	55.0	460 MW
30.0	55.0	1015.0	65.0	430 MW
🔍 Model Training Details
Dataset: 9568 records (from 2006-2011)
Algorithm Used: RandomForestRegressor
R² Score: ~0.95 (High accuracy)
Model File: CCPP.pkl
📌 Future Enhancements
Deploy on AWS/Heroku
Improve UI with Bootstrap/React.js
Test with XGBoost & Deep Learning

📜 Author & Contact
👨‍💻 Bandi Bala Subrahmanyam
📧 balubandi83@gmail.com


