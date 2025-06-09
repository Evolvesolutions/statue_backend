from rest_framework import serializers
from .models import Statue
from .models import Home_list

class StatueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statue
        fields = '__all__'





class Home_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home_list
        fields = '__all__'


