from rest_framework import serializers
from .models import *


class UserSerilizer(serializers.ModelSerializer):
    "It Will Help to Show Data Of User"
    class Meta:
        fields = ["user_id","email","date_joined","is_verified"]
        model = User