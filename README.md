# 🌟 Aura Check – AI-Powered Stress Level Analysis Tool

**Aura Check** is a full-stack, AI-powered web application designed to help users assess, understand, and manage their stress levels through structured questionnaires, machine learning predictions, and personalized insights.

The platform combines **modern web design**, **machine learning**, and **data-driven decision-making** to deliver a seamless mental well-being assessment experience.

---

## 🔗 Live Demo

🚀 **Demo URL:**  
> _Coming Soon_ (will be updated after deployment)

---

## 🧠 What Aura Check Does

Aura Check helps users:

- Assess their stress levels through a structured questionnaire.
- Predict stress, anxiety, and depression scores using trained ML models.
- Gain awareness about their mental well-being through data-backed insights.
- Access helpful coping strategies and informational content.
- Navigate a clean, interactive, and responsive web interface.

---

## ✨ Key Features

✅ User-friendly Login & Quiz Interface  
✅ Automated Stress, Anxiety & Depression Prediction  
✅ Machine Learning–based Score Estimation  
✅ Cleaned & Preprocessed Psychological Dataset  
✅ Boosting Models for Improved Prediction Accuracy  
✅ Multi-page Responsive Web UI  
✅ Secure and Privacy-Focused Design  
✅ Integrated Backend + Frontend ML Pipeline  

---

## 🤖 Machine Learning Highlights

### 🔹 Data Preparation
- Cleaned raw questionnaire responses.
- Handled missing values and categorical encoding.
- Applied one-hot encoding for high-cardinality features.
- Ensured strict feature alignment between training and inference.

### 🔹 Models Used
- **XGBoost**
- **Gradient Boosting**
- **Random Forest**

These models were trained to predict:
- Stress Level
- Anxiety Level
- Depression Level

### 🔹 Model Evaluation
- RMSE (Root Mean Squared Error)
- R² Score

Models were selected based on performance and stability during validation.

### 🔹 Deployment-Ready Inference
- Feature-shape consistency enforced at runtime.
- Optimized preprocessing pipeline for real-time predictions.
- Backend predictions integrated seamlessly with frontend UI.

---

## 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Responsive UI with custom animations
- Font Awesome icons

### Backend
- Python
- Flask
- Flask-RESTful
- Flask-CORS
- Gunicorn (production server)

### Machine Learning
- Scikit-learn
- XGBoost
- Pandas
- NumPy

### Tools & Platforms
- Git & GitHub
- Render (Deployment)
- Microsoft Forms (Questionnaire Input)
- Jupyter Notebook (Model Development)

---

## 🗂 Project Structure

Aura_Check/
│
├── app.py # Flask application
├── script.py # ML preprocessing & prediction logic
├── requirements.txt
│
├── templates/ # HTML templates
│ ├── index.html
│ ├── quiz.html
│ ├── schedule.html
│ └── tech.html
│
├── static/ # CSS, images, assets
│ ├── css/
│ └── img/
│
├── models/ # Trained ML models (.pkl)
└── Scripts/
└── onehot_columns.pkl # Feature alignment file


---

## 🚀 Deployment

The application is deployed using **Render** with:
- `gunicorn` as the production WSGI server
- Environment-based port handling
- Optimized for free-tier cloud hosting

---

## 🔐 Privacy & Security

- No sensitive user data is stored.
- Predictions are generated dynamically at runtime.
- Designed with user confidentiality in mind.

---

## 📌 Future Enhancements

- User authentication with sessions
- Database integration for progress tracking
- Visualization dashboards for stress trends
- Model explainability (SHAP)
- Email or notification-based reminders

---

## 👨‍💻 Author

**Aura Check** was built as a hackathon and portfolio project to demonstrate:

- End-to-end ML deployment
- Real-world preprocessing challenges
- Full-stack application development
- AI integration in mental health applications

---
