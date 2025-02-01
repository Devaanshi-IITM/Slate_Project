from rest_framework import serializers
from django.contrib.auth.models import User # django has the inbuilt user 


# response class to send response
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')    # pass ay field that we want 

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    #create or register new user
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'],
            validated_data['password'],
            
        )
        return user
        
# for login
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only = True)


