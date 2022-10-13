from .utils import create_token,get_payload
from rest_framework import response, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from . import models
# Create your views here.

@api_view(['POST'])
def register_api(request):
    serializer = UserSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    instance = models.User()
    instance.first_name = request.data["first_name"]
    instance.last_name = request.data["last_name"]
    instance.email = request.data["email"]
    instance.set_password(request.data["password"])
    instance.save()
    return response.Response(data=serializer.data)

@api_view(['POST'])
def login_api(request):
    email = request.data["email"]
    password = request.data["password"]
    user= models.User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed("Invalid Credentials")
    if not user.check_password(raw_password=password):
        raise exceptions.AuthenticationFailed("Invalid Credentials")

    token = create_token(user_id = user.id)
    resp = response.Response()
    resp.set_cookie(key='jwt',value=token,httponly=True)
    resp.data = {
        'jwt':token
    }
    return resp

@api_view(['POST'])
def logout_api(request):
    response = response.Response()
    response.delete_cookie('jwt')
    response.data = {
        'message':'success'
    }
    return response

@api_view(['GET'])
def user_api(request):
    token = request.COOKIES.get('jwt')
    payload = get_payload(token)
    user= models.User.objects.filter(id = payload['id']).first()
    serializer = UserSerializer(user)
    return response.Response(serializer.data)


    
    


