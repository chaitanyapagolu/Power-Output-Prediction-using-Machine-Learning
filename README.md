# prediction-of-full-load-electrical-power-output-of-a-base-load-operated-combined-cycle-power-plant

⚡ Power Output Prediction using Machine Learning

📌 Project Overview
This project predicts the full load electrical power output of a Combined Cycle Power Plant (CCPP) using Machine Learning (ML).
By analyzing key ambient conditions such as temperature, exhaust vacuum, ambient pressure, and relative humidity, the model provides accurate energy output predictions.

🚀 Key Features
✅ Predicts Power Output (MW) from input parameters
✅ User-friendly Flask web application
✅ Interactive UI with background styling
✅ Uses a trained Machine Learning model (Random Forest Regressor)

🛠️ Technologies Used
Category	Tools & Libraries
Programming	Python
Libraries	Flask, NumPy, Pandas, Scikit-Learn, Pickle
Frontend	HTML, CSS, JavaScript
Backend	Flask, Python
Visualization	Matplotlib, Seaborn
📂 Project Structure
graphql
Copy
Edit
CCPP_Prediction/
│── app.py                      # Flask backend
│── train_model.py               # Model Training
│── CCPP.pkl                     # Saved Machine Learning Model
│── your_dataset.csv             # Power Plant Dataset
│── templates/                   # HTML Files for UI
│   │── home.html                 # Home Page
│   │── index.html                # Prediction Page
│── static/                      # CSS & JS
│   │── main.css                  # Styling
│   │── background.jpg            # UI Background Image
│── README.md                     # Project Documentation
📥 Setup Instructions
1️⃣ Install Required Libraries
Before running the project, install dependencies:

sh
Copy
Edit
pip install flask numpy pandas scikit-learn matplotlib seaborn pickle5
2️⃣ Run the Flask Web Application
sh
Copy
Edit
python app.py
The server will start at:

cpp
Copy
Edit
http://127.0.0.1:5000/
3️⃣ Open in Your Browser
Visit http://127.0.0.1:5000/
Click "Start Prediction"
Enter input values and click "Predict"
📊 How to Use the Application
1️⃣ Open the Prediction Page
2️⃣ Enter input values for:

AT (Temperature in °C)
V (Exhaust Vacuum in cm Hg)
AP (Ambient Pressure in mbar)
RH (Relative Humidity in %)
3️⃣ Click Predict
4️⃣ View Predicted Power Output (MW)
📌 Sample Inputs & Outputs
AT (°C)	V (cm Hg)	AP (mbar)	RH (%)	Predicted Power Output (MW)
20.5	50.2	1010.3	60.5	455.01 MW
25.0	40.0	1005.0	55.0	460 MW
30.0	55.0	1015.0	65.0	430 MW
22.0	45.5	1012.0	62.0	455 MW
🔍 Model Training Details
Dataset Description
Total Records: 9568
Features Used:
AT - Ambient Temperature (°C)
V - Exhaust Vacuum (cm Hg)
AP - Ambient Pressure (mbar)
RH - Relative Humidity (%)
Target Variable: PE (Power Output in MW)
Machine Learning Model
Algorithm Used: RandomForestRegressor
Model Performance:
R² Score on Training Data: 0.98
R² Score on Test Data: 0.95
Saved Model: CCPP.pkl
📌 Future Improvements
🔹 Add more ML models like Gradient Boosting, XGBoost
🔹 Deploy on Heroku/AWS for online access
🔹 Improve UI with Bootstrap/React.js

💡 Contributors
👨‍💻 Bandi Bala Subrahmanyam
📧 balubandi83@gmail.com
🔗 LinkedIn
🔗 GitHub

📜 License
This project is open-source and can be freely used for educational purposes.

