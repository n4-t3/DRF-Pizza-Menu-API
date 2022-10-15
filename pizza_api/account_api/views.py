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

@api_view(['GET','POST'])
def orders_api(request):
    if request.method == 'GET':
        orders = models.Order.objects.filter(user=request.user)
        content = {'orders':[]}
        for order in orders:
            serializer = OrderSerializer(order)
            content['orders'].append(serializer.data)
        resp = response.Response()
        resp.data = content
        return resp
    elif request.method == 'POST':
        serializedOrder = OrderSerializer(data = request.data)
        serializedOrder.is_valid(raise_exception=True)
        data = serializedOrder.validated_data
        instance = models.Order()
        instance.user = models.User.objects.filter(id=request.user.id).first()
        instance.item = data["item"]
        instance.extras = data['extras']
        instance.delivery_status = data['delivery_status']
        instance.save()
        return response.Response(data=serializedOrder.data)


@api_view(['GET','PUT','DELETE'])
def order_chosen(request,id):
    if request.method == "GET":
        try:
            order = models.Order.objects.get(id=id)
        except:
            return response.Response({'Error': 'order not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return response.Response(serializer.data)
    if request.user.is_authenticated:
        if request.method == "PUT":
            order = models.Order.objects.get(id=id)
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data)
            else:
                return response.Response(serializer.errors)
        elif request.method=="DELETE":
            order = models.Order.objects.get(id=id)
            order.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT" or request.method=="DELETE":
        return response.Response({'Error': 'Authentication credentials were not provided.'}, status=status.HTTP_403_FORBIDDEN)

