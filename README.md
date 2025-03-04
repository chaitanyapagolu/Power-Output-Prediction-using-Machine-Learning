 Power Output Prediction using Machine Learning
📌 Project Overview
This project predicts the electrical power output of a Combined Cycle Power Plant (CCPP) using Machine Learning.
By analyzing ambient temperature, exhaust vacuum, ambient pressure, and relative humidity, the model predicts power output in megawatts (MW).

🔹 Key Features
✅ Predicts power output based on input parameters
✅ User-friendly web interface using Flask
✅ Machine Learning model trained using Random Forest Regressor
✅ Simple and easy-to-use UI

🛠️ Technologies Used
Programming Language: Python
Libraries: Flask, NumPy, Pandas, Scikit-Learn, Pickle
Frontend: HTML, CSS
Backend: Flask Web Framework
Data Visualization: Matplotlib, Seaborn
📂 Project Structure
graphql
Copy
Edit
CCPP_Prediction/
│── app.py                  # Flask backend application
│── train_model.py           # Model training script
│── CCPP.pkl                 # Trained Machine Learning model
│── your_dataset.csv         # Dataset used for training
│── templates/               # HTML files for UI
│   │── home.html            # Home Page
│   │── index.html           # Prediction Page
│── static/                  # CSS and images
│   │── main.css             # Styling for UI
│   │── background.jpg       # Background image
│── README.md                # Project documentation
📥 Installation & Setup
1️⃣ Install Required Libraries
Run the following command to install the necessary dependencies:

sh
Copy
Edit
pip install flask numpy pandas scikit-learn matplotlib seaborn pickle5
2️⃣ Run the Flask Application
Start the Flask web server by running:

sh
Copy
Edit
python app.py
After running the command, open your browser and visit:

cpp
Copy
Edit
http://127.0.0.1:5000/
📊 How to Use the Application
1️⃣ Open http://127.0.0.1:5000/ in a web browser.
2️⃣ Click "Start Prediction" to go to the input page.
3️⃣ Enter the following input values:

AT (Ambient Temperature in °C)
V (Exhaust Vacuum in cm Hg)
AP (Ambient Pressure in mbar)
RH (Relative Humidity in %)
4️⃣ Click "Predict" and view the predicted power output in megawatts (MW).
📌 Sample Inputs & Expected Outputs
AT (°C)	V (cm Hg)	AP (mbar)	RH (%)	Predicted Power Output (MW)
20.5	50.2	1010.3	60.5	455.01 MW
25.0	40.0	1005.0	55.0	460 MW
30.0	55.0	1015.0	65.0	430 MW
22.0	45.5	1012.0	62.0	455 MW
🔍 Model Training Details
📌 Dataset Description
Total Records: 9568
Features Used:
AT - Ambient Temperature (°C)
V - Exhaust Vacuum (cm Hg)
AP - Ambient Pressure (mbar)
RH - Relative Humidity (%)
Target Variable: PE (Power Output in MW)
📌 Machine Learning Model
Algorithm Used: RandomForestRegressor
Model Performance:
R² Score on Training Data: 0.98
R² Score on Test Data: 0.95
Saved Model: CCPP.pkl
📌 Future Improvements
🔹 Improve UI with Bootstrap/React.js
🔹 Deploy on Heroku/AWS for online access
🔹 Experiment with other ML models (XGBoost, Neural Networks)

💡 Author & Contact
👨‍💻 Bandi Bala Subrahmanyam
📧 balubandi83@gmail.com
🔗 LinkedIn
🔗 GitHub

📜 License
This project is open-source and can be freely used for educational purposes.

