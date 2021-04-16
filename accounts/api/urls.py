from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import registration_api, LoginAPIView

app_name = "accounts"
urlpatterns = [
    path("register", csrf_exempt(registration_api), name="register"),
    path("login", LoginAPIView.as_view(), name="login"),
]