from rest_framework import serializers
from .models import Menu
from .utils import optimize_image
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"
    picture = serializers.ImageField(allow_empty_file=False, use_url=True,required=False)
    


    