# 💧 Water Quality Prediction Web App

A machine learning-based web application developed using Flask that predicts the safety of water for drinking or usage purposes through three different input methods — TDS & pH, survey-based parameters, and more.

## 🚀 Features

- 🔍 **Three input methods**:
  - **TDS & pH**: Ideal for general users using simple measuring tools.
  - **Survey-Based Form**: For detailed input (6–8 parameters such as turbidity, conductivity, etc.).
  - **Alternate Suggestions**: Provides purification tips and usage suggestions based on input.

- ⚙️ **Machine Learning Integration**:
  - Trained multiple models (Decision Tree, SVM, Logistic Regression).
  - Finalized **Random Forest** with **hyperparameter tuning** for highest accuracy.

- 🌐 **Frontend**:
  - Built using **HTML**, **CSS**, and **Vanilla JavaScript**.
  - Simple, responsive, and user-friendly interface.

## 🧠 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **ML Libraries**: Scikit-learn, NumPy, Pandas
- **Data Visualization**: Matplotlib (if applicable)

## 🧪 Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Water-Quality-Prediction-Model.git
   cd Water-Quality-Prediction-Model
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open in browser:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📂 Project Structure

```
Water-Quality-Prediction-Model/
│
├── static/             # CSS, JS files
├── templates/          # HTML templates
├── models/             # Trained ML models
├── app.py              # Flask main app
├── requirements.txt    # Dependencies
├── README.md           # Project README
└── ...
```

## 📊 Dataset

Used water quality datasets with parameters like:
- Turbidity
- Conductivity
- pH
- TDS
- Temperature
- Hardness

## 📌 Future Enhancements

- Add real-time IoT integration for live data input
- Extend model to detect industrial water usability
- Deploy on cloud (e.g., Render, AWS)

## 👨‍💻 Author
Tarun Gautam

---

📌 *This project was built as part of an effort to improve accessibility to water safety information through intelligent, user-friendly interfaces.*  
```
