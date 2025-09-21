from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .model_loader import predict_price


@csrf_exempt
def predict(request):
if request.method == 'POST':
data = json.loads(request.body.decode('utf-8'))
location = data.get('location')
sqft = data.get('sqft')
bath = data.get('bath')
bhk = data.get('bhk')


try:
price = predict_price(location, sqft, bath, bhk)
return JsonResponse({'predicted_price_lakhs': round(float(price), 2)})
except Exception as e:
return JsonResponse({'error': str(e)}, status=400)
else:
return JsonResponse({'error': 'Only POST allowed'}, status=405)
