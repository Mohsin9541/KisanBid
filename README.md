# 🌾 KisanBid – AI-Powered Agricultural Bidding Platform

**KisanBid** is an AI-powered agricultural bidding platform designed to help farmers list their crops, connect with buyers across India, and make more informed pricing decisions.

The project uses Machine Learning to estimate recommended starting bid prices based on crop characteristics, location, quality, quantity, weather conditions, and historical market information.

---

## 🎯 Project Objectives

* Help farmers make informed decisions when setting crop starting prices.
* Connect farmers from Jammu & Kashmir with potential buyers across India.
* Use Machine Learning to estimate crop starting bid prices.
* Explore agricultural market trends through data analysis and visualization.
* Demonstrate how AI can support digital agricultural marketplaces.

## ✨ Key Features

* **Crop Price Prediction:** Estimates recommended starting bid prices using a trained regression model.
* **Exploratory Data Analysis:** Analyzes agricultural data to identify patterns and relationships.
* **Data Visualization:** Uses charts and graphs to understand crop prices and market trends.
* **Machine Learning:** Compares multiple regression algorithms to identify a suitable prediction model.
* **Agricultural Insights:** Considers crop type, variety, quality, quantity, location, and market conditions.

## 🤖 Machine Learning Approach

KisanBid uses a supervised Machine Learning regression approach to predict crop starting bid prices.

### Algorithms Implemented

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor

### Selected Model

**Random Forest Regressor**

The models are evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

The model with the lowest MAE is selected according to the evaluation results.

### Input Features

The prediction system considers:

* District
* Crop
* Crop Variety
* Quality Grade
* Agricultural Season
* Crop Quantity
* Quality Score
* Storage Type
* Distance to Major Mandi
* Transportation Cost
* Recent Rainfall
* Average Temperature
* Market Arrival Quantity
* Historical Modal Market Price
* Year and Month

### Prediction Output

The model generates an estimated starting bid price in **Indian Rupees (INR) per quintal**.

---

## 🛠️ Technologies Used

| Technology       | Purpose                            |
| ---------------- | ---------------------------------- |
| Python           | Main programming language          |
| Pandas           | Data manipulation and analysis     |
| NumPy            | Numerical computations             |
| Matplotlib       | Data visualization                 |
| Seaborn          | Statistical visualization          |
| Scikit-learn     | Machine Learning and preprocessing |
| Joblib           | Saving and loading trained models  |
| Jupyter Notebook | EDA and ML experimentation         |
| Streamlit        | Web application development        |

---

## 📊 Project Workflow

```text
Agricultural Dataset
        |
        v
Data Collection
        |
        v
Exploratory Data Analysis
        |
        v
Data Cleaning & Preprocessing
        |
        v
Feature Selection
        |
        v
Train-Test Split
        |
        v
Machine Learning Models
        |
        v
Model Evaluation
        |
        v
Best Model Selection
        |
        v
Model Serialization
        |
        v
KisanBid Application
        |
        v
Crop Starting Price Prediction
```

---

## 📁 Project Structure

```text
KisanBid/
│
├── dataset/
│   └── jk_farm_bidding_eda_dataset.csv
│
├── models/
│   └── kisanbid_model.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   └── ML_Implementation.ipynb
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

*Note: Update the folder and notebook names above to match your actual repository structure.*

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/KisanBid.git
```

### 2. Navigate to the Project Directory

```bash
cd KisanBid
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📈 Future Improvements

* Integrate verified real-world agricultural market datasets.
* Develop a complete online bidding and auction system.
* Add secure farmer and buyer authentication.
* Integrate payment gateways.
* Provide real-time market price updates.
* Introduce multilingual support for farmers.
* Develop a mobile-friendly application.
* Improve model performance using additional historical market data.

---

## ⚠️ Dataset Disclaimer

The dataset used in this project is intended for educational and experimental purposes. If synthetic data is used, model predictions should not be considered verified real-world market prices.

Actual agricultural price estimation requires reliable historical market data and validation against real market conditions.

---

## 👨‍💻 Developer

**Mohsin Nawaz**

B.Tech – Computer Science and Engineering
Specialization: Data Science and Machine Learning

---

## 📜 License

This project is developed for educational and academic purposes.
