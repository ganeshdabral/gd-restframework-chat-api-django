from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.contrib.auth.models import User

@api_view(["POST",])
@permission_classes([])
@authentication_classes([])
def registration_api(request):
    data = {}
    email = request.data.get('email', '0').lower()
    if validate_email(email) != None:
        data['error_message'] = 'That email is already in use.'
        data['response'] = 'Error'
        return Response(data)

    username = request.data.get('username', '0')
    if validate_username(username) != None:
        data['error_message'] = 'That username is already in use.'
        data['response'] = 'Error'
        return Response(data)

    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'successfully registered new user.'
        data['email'] = account.email
        data['username'] = account.username
        data['pk'] = account.pk
        token = Token.objects.get(user=account).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)

def validate_email(email):
    account = None
    try:
        account = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    if account != None:
        return email

def validate_username(username):
    account = None
    try:
        account = User.objects.get(username=username)
    except User.DoesNotExist:
        return None
    if account != None:
        return username

class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        context = {}

        username = request.POST.get('username')
        password = request.POST.get('password')
        account = authenticate(username=username, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            context['response'] = 'Successfully authenticated.'
            context['pk'] = account.pk
            context['username'] = username
            context['email'] = account.email
            context['token'] = token.key
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'

        return Response(context)