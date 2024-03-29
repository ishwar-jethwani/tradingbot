from genericpath import exists
import json
from dj_rest_auth.views import LoginView
from .serializers import *
from rest_framework.generics import *
import random
from django.template.loader import get_template
from django.core.mail import send_mail
import jwt
from TradingBot.constants import KEY_FOR_OTP
from rest_framework.response import Response
from rest_framework import status

class CustomLoginView(LoginView):
    "Custom Login View"
      
    def get_response(self):
        orginal_response = super().get_response()
        return orginal_response
        # final_response = orginal_response["user"]
        # final_response.update({"access_token":orginal_response["orginal_response"],"refresh_token":orginal_response["refresh_token"]})
        # return final_response

class EmailVerification(ListAPIView):
    "User Email Verification class"
    serializer_class = VerificationSerializer
    otp = random.randint(1000,9999)
    def get(self, request):
        email = request.GET.get("email")
        html = get_template("email.html")
        html_data = html.render({"otp":self.otp})
        key = KEY_FOR_OTP
        encoded_value = jwt.encode({"otp":self.otp},key,algorithm="HS256")
        subject = "Email Verification"
        send_mail(
            from_email = None,
            recipient_list = [email],
            subject =subject,
            html_message = html_data,
            message = f"This is you otp:{self.otp} to verify email."
            )
        return Response({"msg":"email has been sent","value":encoded_value},status=status.HTTP_200_OK)

class ResetPassword(ListAPIView):
    otp = random.randint(1000,9999)
    def get(self,request):
        email = request.GET.get("email")
        if User.objects.filter(email=email).exists():
            html = get_template("reset.html")
            html_data = html.render({"otp":self.otp})
            key = KEY_FOR_OTP
            encoded_value = jwt.encode({"otp":self.otp},key,algorithm="HS256")
            subject = "OTP for Reset Password"
            send_mail(
                from_email = None,
                recipient_list = [email],
                subject =subject,
                html_message = html_data,
                message = f"This is you otp:{self.otp} to verify email."
                )
            return Response({"msg":"email has been sent","value":encoded_value},status=status.HTTP_200_OK)
        return Response({"msg":"please enter registered email id"})   
    def post(self,request):
        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.filter(email=email)
        if user.exists():
            user = user.first()
            user.set_password(password)
            user.save()
            return Response({"msg":"password is set sucessfully"},status=status.HTTP_200_OK)
        return Response({"msg":"please enter registered email id"})   


        




        


