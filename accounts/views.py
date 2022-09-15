from django.shortcuts import render
from dj_rest_auth.views import LoginView
from .serializers import *

class CustomLoginView(LoginView):
    "Custom Login View"
      
    def get_user(self):
        serilize = UserSerilizer(self.request.user)
        return serilize.data
        
    def get_response(self):
        orginal_response = super().get_response()
        mydata = self.get_user()
        orginal_response.data.update(mydata)
        return orginal_response




