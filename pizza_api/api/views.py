from .models import Menu
from .serializers import MenuSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes,parser_classes
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FormParser,MultiPartParser
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

# @renderer_classes([JSONRenderer])
@parser_classes([MultiPartParser,FormParser])
@api_view(['GET','POST'])
@swagger_auto_schema(
    operation_summary='Register User',
    operation_description='This endpoint allows you to register a new user.',
    request_body=MenuSerializer
)
def menu_list(request,format=None):
    if request.method =='GET':
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        if request.user.is_authenticated and request.user.is_staff:
            serializer = MenuSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                instance = Menu()
                instance.name = data["name"]
                instance.price = data["price"]
                if "topping_1" in request.POST:
                    instance.topping_1 = request.POST["topping_1"]
                if "topping_2" in request.POST:
                    instance.topping_2 = request.POST["topping_2"]
                if "topping_3" in request.POST:
                    instance.topping_3 = request.POST["topping_3"]
                if "size" in request.POST:
                    instance.size = request.POST["size"]
                if "our_rating" in request.POST:
                    instance.our_rating = request.POST["our_rating"]
                if "items_in_stock" in request.POST:
                    instance.items_in_stock = request.POST["items_in_stock"]
                if "picture" in request.FILES:
                    instance.picture = request.FILES["picture"]
                instance.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error': 'Authentication credentials were not provided or user not staff.'}, status=status.HTTP_403_FORBIDDEN)

# @renderer_classes([JSONRenderer])
@api_view(['GET','PUT','DELETE'])
@swagger_auto_schema(
    request_body=MenuSerializer
)
def menu_chosen(request,id):
    if request.method == "GET":
        try:
            menu = Menu.objects.get(id=id)
            serializer = MenuSerializer(menu)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'Error': 'Menu not found'}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "PUT" or request.method=="DELETE":  
        if request.user.is_authenticated:
            if request.method == "PUT":
                menu = Menu.objects.get(id=id)
                serializer = MenuSerializer(menu, data=request.data)
                if serializer.is_valid():
                    if "picture" not in request.FILES:
                        serializer.validated_data["picture"] = menu.picture
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method=="DELETE":
                if not request.user.is_staff:
                    return Response({'Error': 'User is not staff.'}, status=status.HTTP_403_FORBIDDEN)
                movies = Menu.objects.get(id=id)
                movies.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'Error': 'Authentication credentials were not provided.'}, status=status.HTTP_403_FORBIDDEN)
        