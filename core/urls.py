from django.urls import path
from . import views
from .views import IndexFormView


app_name = 'core'

urlpatterns = [
    path('data/', views.json_view, name='json_view'),
    path('', IndexFormView.as_view(), name='index'),
]
