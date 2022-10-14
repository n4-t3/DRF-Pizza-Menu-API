from .models import Menu
from .serializers import MenuSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
from rest_framework import status
from rest_framework.renderers import JSONRenderer
# Create your views here.

# @renderer_classes([JSONRenderer])
@api_view(['GET','POST'])
def menu_list(request):
    if request.method =='GET':
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        if request.user.is_authenticated:
            serializer = MenuSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response({'Error': 'Authentication credentials were not provided.'}, status=status.HTTP_403_FORBIDDEN)

# @renderer_classes([JSONRenderer])
@api_view(['GET','PUT','DELETE'])
def menu_chosen(request,id):
    if request.method == "GET":
        try:
            menu = Menu.objects.get(id=id)
        except:
            return Response({'Error': 'Menu not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)
    if request.user.is_authenticated:
        if request.method == "PUT":
            menu = Menu.objects.get(id=id)
            serializer = MenuSerializer(menu, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        elif request.method=="DELETE":
            movies = Menu.objects.get(id=id)
            movies.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT" or request.method=="DELETE":
        return Response({'Error': 'Authentication credentials were not provided.'}, status=status.HTTP_403_FORBIDDEN)
    