from django.urls import path
from .views import Login, Register

urlpatterns = [
    path('login/', Login),
    path('register/', Register)
]
