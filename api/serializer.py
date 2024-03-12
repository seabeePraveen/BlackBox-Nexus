from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Solution
from django.http import JsonResponse

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','username','password']
        
    def create(self,validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class SolutionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Solution
        fields = ['user','questionID','code','extention']


class SolvedQuestionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Solution
        fields = ['questionID','code']

