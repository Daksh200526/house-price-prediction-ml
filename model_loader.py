import os
import joblib
import pandas as pd
from django.conf import settings


MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor_app', 'house_price_model.pkl')
_model = None




def load_model():
global _model
if _model is None:
_model = joblib.load(MODEL_PATH)
return _model




def predict_price(location, sqft, bath, bhk):
model = load_model()
x = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'BHK'])
return model.predict(x)[0]
