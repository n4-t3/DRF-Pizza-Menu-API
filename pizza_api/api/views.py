from .models import Menu
from .serializers import MenuSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes,parser_classes
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import FormParser,MultiPartParser
from .utils import optimize_image
# Create your views here.

# @renderer_classes([JSONRenderer])
# @parser_classes([MultiPartParser,FormParser])
@api_view(['GET','POST'])
def menu_list(request,format=None):
    if request.method =='GET':
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        if request.user.is_authenticated:
            serializer = MenuSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                instance = Menu()
                instance.name = data["name"]
                instance.price = data["price"]
                if "topping_1" in data:
                    instance.topping_1 = data["topping_1"]
                if "topping_2" in data:
                    instance.topping_2 = data["topping_2"]
                if "topping_3" in data:
                    instance.topping_3 = data["topping_3"]
                if "size" in data:
                    instance.size = data["size"]
                if "average_rating" in data:
                    instance.average_rating = data["average_rating"]
                if "number_of_ratings" in data:
                    instance.number_of_ratings = data["number_of_ratings"]
                if "picture" in request.FILES:
                    image = optimize_image(request.FILES["picture"])
                    instance.picture = image
                instance.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Error': 'Authentication credentials were not provided.'}, status=status.HTTP_403_FORBIDDEN)

# @renderer_classes([JSONRenderer])
@api_view(['GET','PUT','DELETE'])
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
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method=="DELETE":
                movies = Menu.objects.get(id=id)
                movies.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'Error': 'Authentication credentials were not provided.'}, status=status.HTTP_403_FORBIDDEN)
        