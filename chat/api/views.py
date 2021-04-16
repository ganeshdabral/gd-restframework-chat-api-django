from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


from chat.models import MsgModel
from chat.api.serializers import ChatSerializer, ViewChatSerializer, UserSerializer
from django.contrib.auth.models import User

@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def send_chat(request,pk):
    chat_obj = MsgModel(sender=request.user)
    try:
        chat_obj.reciver = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'sending to invalid user'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ChatSerializer(chat_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def view_chat(request,pk):
    try:
        reciver_obj = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'you fetch the invalid user chat'}, status=status.HTTP_400_BAD_REQUEST)
    error = {}
    if reciver_obj:
        chat_obj = MsgModel.objects.filter(Q(sender=request.user, reciver=reciver_obj) | Q(sender=reciver_obj, reciver=request.user)).order_by('id')
        serializer = ViewChatSerializer(chat_obj, many=True)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    return Response(error, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def user_list(request):
    user_obj = User.objects.all().exclude(id=request.user.id)
    serializer = UserSerializer(user_obj, many=True, context={'request': request})
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)