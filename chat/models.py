from django.db import models
from django.contrib.auth.models import User


class MsgModel(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sender')
    reciver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='reciver')
    content = models.TextField(max_length=500)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
