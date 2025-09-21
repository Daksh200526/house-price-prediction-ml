from django.urls import path
from . import views


urlpatterns = [
path('predict/', views.predict, name='predict'),
]




# myproject/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
path('admin/', admin.site.urls),
path('', include('predictor_app.urls')),
]
