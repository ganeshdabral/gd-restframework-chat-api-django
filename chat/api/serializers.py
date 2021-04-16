from rest_framework import routers, serializers
from chat.models import MsgModel
from django.contrib.auth.models import User
from django.db.models import Q

class ChatSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField('get_sender_methord')
    reciver = serializers.SerializerMethodField('get_reciver_methord')
    class Meta:
        model = MsgModel
        fields = ['id', 'sender', 'reciver', 'content']

    def get_sender_methord(self, user_obj):
        username =  user_obj.sender.username
        return username

    def get_reciver_methord(self,user_obj):
        username = user_obj.reciver.username
        return username


class ViewChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MsgModel
        fields = ['id', 'sender', 'reciver', 'content']

class UserSerializer(serializers.ModelSerializer):
    chat = serializers.SerializerMethodField('get_chat')
    class Meta:
        model = User
        fields = ['id', 'username', 'email','chat']

    def get_chat(self,user_obj):
        user = self.context['request'].user
        chat_obj = MsgModel.objects.filter(Q(sender=user, reciver=user_obj) | Q(sender=user_obj, reciver=user)).order_by('id')
        serializer = ViewChatSerializer(chat_obj, many=True)
        return serializer.data
