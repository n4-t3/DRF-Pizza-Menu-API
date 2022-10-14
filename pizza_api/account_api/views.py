from rest_framework import response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import UserSerializer
from . import models
# Create your views here.


@api_view(['POST'])
def register_api(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    instance = models.User()
    instance.first_name = data["first_name"]
    instance.last_name = data["last_name"]
    instance.email = data["email"]
    instance.set_password(data["password"])
    instance.save()
    return response.Response(data=serializer.data)


@api_view(['GET'])
def user_api(request):
    try:
        user = models.User.objects.filter(id=request.user.id).first()
        content = {'user_id': user.id, 'user_email': user.email, 'staff':user.is_staff}
        return response.Response(content)
    except:
        return response.Response('Invalid credentials')
