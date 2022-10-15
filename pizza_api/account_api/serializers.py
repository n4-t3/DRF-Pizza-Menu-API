from rest_framework import fields, serializers
from .models import Order, SIDES_CHOICES, DELIVERY_CHOICES

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only = True)


class CustomMultipleChoiceField(fields.MultipleChoiceField):
    def to_representation(self, value):
        return list(super().to_representation(value))


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    extras = CustomMultipleChoiceField(choices=SIDES_CHOICES)
    delivery_status = CustomMultipleChoiceField(choices=DELIVERY_CHOICES)


    