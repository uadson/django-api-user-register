from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('data/', views.json_view, name='json_view'),
]
