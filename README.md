# 🏠 Bengaluru House Price Prediction (Django Backend)

This project is a **Django-based backend API** that predicts house prices in Bengaluru using a Machine Learning model trained in Jupyter Notebook.

---

## 🚀 Features

* Trained ML pipeline (with preprocessing + model) exported from Jupyter Notebook.
* Django backend with a `/predict/` API endpoint.
* Accepts input features (`location`, `sqft`, `bath`, `bhk`) and returns predicted house price in **Lakhs**.
* Model file (`house_price_model.pkl`) stored in the Django app for fast loading.

---

## 📂 Project Structure

```
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   └── urls.py
├── predictor_app/
│   ├── house_price_model.pkl        # trained model file (exported from Jupyter)
│   ├── model_loader.py              # loads model + predict function
│   ├── views.py                     # API endpoint for predictions
│   ├── urls.py                      # app-level URLs
│   └── apps.py
└── README.md
```

---

## 🧑‍💻 Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd myproject
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Export Model from Jupyter

In your Jupyter Notebook after training the `best_model`:

```python
import joblib
joblib.dump(best_model, 'house_price_model.pkl')
```

Move `house_price_model.pkl` into `predictor_app/`.

### 4. Run Django Server

```bash
python manage.py migrate
python manage.py runserver
```

Server will start at: `http://127.0.0.1:8000/`

---

## 📡 API Usage

### Endpoint:

`POST /predict/`

### Request Body (JSON):

```json
{
  "location": "Whitefield",
  "sqft": 2000,
  "bath": 2,
  "bhk": 2
}
```

### Response (JSON):

```json
{
  "predicted_price_lakhs": 125.4
}
```

---

## 🛠 Requirements

* Python 3.8+
* Django
* scikit-learn
* pandas
* joblib

Install all using:

```bash
pip install -r requirements.txt
```

---

## 📌 Notes

* Ensure the **same scikit-learn version** is used in Jupyter Notebook and Django environment.
* Place the `.pkl` file inside `predictor_app/`.
* This repo provides only the **backend API**. You can extend it with a frontend form or connect it to a React/Angular app.

---

## 🔮 Future Enhancements

* Add frontend form for manual input.
* Deploy on cloud (Heroku, AWS, or Azure).
* Add more features (balcony, furnishing, etc.) into the model.
