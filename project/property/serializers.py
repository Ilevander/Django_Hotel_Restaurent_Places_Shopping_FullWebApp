from rest_framework import serializers
from .models import Property

'''Django REST framework is a powerful and flexible toolkit for building Web APIs.
'''
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        