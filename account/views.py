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
        email = mydata["email"]
        username = mydata["username"]
        # subject = "Ultra Creation Sending Email"
        # message = "Hi %s! Welcome to UltraXpert" % email
        # htmly = get_template("welcome-email.html")
        # htmly = htmly.render({"username":username})
        User.objects.filter(email=email).update(is_verified=True)
        # send_mail(
        #     from_email = None,
        #     recipient_list = [email],
        #     subject =subject,
        #     html_message = htmly,
        #     message = message
        #     )

        return orginal_response


