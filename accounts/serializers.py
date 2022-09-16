from rest_framework import serializers
from .models import *
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerilizer(serializers.ModelSerializer):
    "It Will Help to Show Data Of User"
    class Meta:
        fields = ["user_id","first_name","last_name","email","date_joined","is_verified"]
        model = User
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data = dict(data)
        user_data = {
            "userId":data["user_id"],
            "emailId":data["email"],
            "joinedDate":data["date_joined"],
            "isVerified":data["is_verified"],
            "firstName":data["first_name"],
            "lastName":data["last_name"]

        }
        return user_data

class CustomRegisterSerializer(RegisterSerializer):
    "Registration serializer for addting more fields while registering user"
    first_name  = serializers.CharField(max_length=10,required=False)
    last_name   = serializers.CharField(max_length=10,required=False)
    is_verified = serializers.BooleanField(default=False,required=False)
    
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict["first_name"] = self.validated_data.get('first_name', '')
        data_dict["last_name"] = self.validated_data.get('last_name','')
        data_dict["is_verified"] = self.validated_data.get('is_verified')
        return data_dict
        
        
class VerificationSerializer(serializers.ModelSerializer):
    "Verification Response Serializer"
    class Meta:
        model = User
        fields = ["user_id","email","is_verified"]
    def to_representation(self, instance):
        data = dict(super().to_representation(instance))
        verification_data = {
            "userId":data["user_id"],
            "emailId":data["email"],
            "isVerified":data["is_verified"]
        }
        return verification_data