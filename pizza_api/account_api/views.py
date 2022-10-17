from rest_framework import response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import UserSerializer,OrderSerializer
from . import models
from api.models import Menu
# Create your views here.


@api_view(['POST'])
def register_api(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        instance = models.User()
        instance.first_name = data["first_name"]
        instance.last_name = data["last_name"]
        instance.email = data["email"]
        instance.set_password(data["password"])
        instance.save()
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
    else:
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_api(request):
    if request.user.is_authenticated:
        user = models.User.objects.filter(id=request.user.id).first()
        content = {'user_id': user.id, 'user_email': user.email, 'staff':user.is_staff}
        return response.Response(data=content, status=status.HTTP_200_OK)
    else:
        return response.Response({'Error': 'Authentication credentials were not provided.'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET','POST'])
def orders_api(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            orders = models.Order.objects.filter(user=request.user)
            serializer = OrderSerializer(orders,many=True)
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)
        elif request.method == "POST":
            request.data["user"] = request.user.id
            serializedOrder = OrderSerializer(data = request.data)
            if serializedOrder.is_valid():
                serializedOrder.save()
                return response.Response(data=serializedOrder.data, status=status.HTTP_200_OK)
            else:
                return response.Response(serializedOrder.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return response.Response({'Error': 'Authentication credentials were not provided.'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET','PUT','DELETE'])
def order_chosen(request,id):
    if request.user.is_authenticated:
        if request.method == "GET":
            try:
                order = models.Order.objects.get(id=id)
                serializer = OrderSerializer(order)
                return response.Response(data=serializer.data, status=status.HTTP_200_OK)
            except:
                return response.Response({'Error': 'order not found'}, status=status.HTTP_404_NOT_FOUND)
        elif request.method == "PUT":
            order = models.Order.objects.get(id=id)
            request.data["user"] = request.user.id
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method=="DELETE":
            order = models.Order.objects.get(id=id)
            order.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return response.Response({'Error': 'Authentication credentials were not provided.'}, status=status.HTTP_403_FORBIDDEN)

