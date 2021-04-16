from django.urls import path
from .views import send_chat, view_chat, user_list
app_name = 'blog'
urlpatterns = [
    path('send/<pk>', send_chat, name="send"),
    path('view/<pk>', view_chat, name="view_chat"),
    path('users', user_list, name="users"),
]