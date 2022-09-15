from rest_framework import serializers
from .models import *


class UserSerilizer(serializers.ModelSerializer):
    "It Will Help to Show Data Of User"
    class Meta:
        fields = ["user_id","email","date_joined","is_verified"]
        model = User
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data = dict(data)
        user_data = {
            "userId":data["user_id"],
            "emailId":data["email"],
            "joinedDate":data["date_joined"],
            "isVerified":data["is_verified"]
        }
        return user_data
        
        
