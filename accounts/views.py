import json
from dj_rest_auth.views import LoginView
from .serializers import *

class CustomLoginView(LoginView):
    "Custom Login View"
      
    def get_response(self):
        orginal_response = super().get_response()
        return orginal_response
        # final_response = orginal_response["user"]
        # final_response.update({"access_token":orginal_response["orginal_response"],"refresh_token":orginal_response["refresh_token"]})
        # return final_response




