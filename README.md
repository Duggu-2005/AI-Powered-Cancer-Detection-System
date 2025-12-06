# 🧬 AI-Powered Cancer Detection System
A complete **Machine Learning + Django + Animated Frontend** system that predicts whether a breast tumor is **Malignant (Cancerous)** or **Benign (Non-Cancerous)** using 30 diagnostic medical features.

---

## 🚀 Features
### 🔍 Machine Learning
- Logistic Regression model
- Trained on Breast Cancer Wisconsin Dataset
- Uses 30 clinical features for prediction
- Includes `model.pkl` and `scaler.pkl`

### 🖥️ Modern Frontend
- Fully animated UI
- GSAP-based transitions
- Gradient backgrounds & dynamic badges
- Responsive & clean design

### 🛠️ Django Backend
- Loads ML model
- Preprocesses input values
- Runs prediction
- Renders animated results

---

## 📂 Project Structure
```
AI-Powered-Cancer-Detection-System/
│
├── manage.py
├── requirements.txt
├── Procfile
│
├── your_app/
│   ├── views.py
│   ├── urls.py
│   ├── model.pkl
│   ├── scaler.pkl
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css, js files
│
└── project_folder/
    ├── settings.py
    └── wsgi.py
```

---

## 🔧 Installation
### 1️⃣ Clone the repository
```
git clone https://github.com/Duggu-2005/AI-Powered-Cancer-Detection-System.git
cd AI-Powered-Cancer-Detection-System
```

### 2️⃣ Create & activate virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Run Django server
```
python manage.py runserver
```
🌐 Open: **http://127.0.0.1:8000**

---

## 🎯 How to Use
1. Enter 30 comma-separated diagnostic values
2. Click **Predict Now**
3. The system returns:
   - **Cancerous (Malignant)**
   - **Not Cancerous (Benign)**

Animated badge displays your prediction.

---

## 🧪 Sample Inputs
### ✔ Benign Example
```
12.05,14.63,78.04,449.3,0.1031,0.09092,0.06592,0.02749,0.1675,0.05913,
0.1786,1.819,1.955,13.99,0.00443,0.01421,0.01502,0.00645,0.01994,0.001875,
13.30,20.37,84.48,546.1,0.1341,0.1751,0.1381,0.05314,0.2934,0.0934
```

### ❗ Malignant Example
```
17.99,10.38,122.80,1001.0,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,
1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,
25.38,17.33,184.6,2019.0,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189
```

---

## ☁️ Render Deployment Steps (Free)
1. Push project to GitHub
2. On Render → **New Web Service**
3. Select your repository
4. Fill:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn project_folder.wsgi`
5. Add environment vars:
```
PYTHON_VERSION = 3.10
DJANGO_SETTINGS_MODULE = project_folder.settings
```
6. Deploy 🚀
7. Render gives a live website URL

---

## ⚠️ Disclaimer
This tool is for **educational purposes only** and should **not** be used as a replacement for professional medical diagnosis.

---

## ⭐ Support
If you like this project, please ⭐ star the GitHub repository!

📧 Contact: **devanshumishra2005@gmail.com**

