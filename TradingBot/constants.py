from decouple import config
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
EMAIL_HOST_USER_NAME  = config("EMAIL_HOST_USER_NAME")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")
KEY_FOR_OTP = config("KEY_FOR_OTP")


