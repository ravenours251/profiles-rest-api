from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class HelloSerializer(serializers.Serializer):
    """Serialize a name field for testing our APIview"""
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Sealizes a user profile object"""

    class Meta:
        model = UserProfile
        fields = ('id','email','name','password')
        extra_kwagrs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            },
        }
    
    def create(self,validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user