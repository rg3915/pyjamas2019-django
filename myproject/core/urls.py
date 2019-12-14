from django.urls import path
from myproject.core.views import index


urlpatterns = [
    path('', index),
]
