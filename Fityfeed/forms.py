from django.forms import ModelFrom
from .models import *
from django.contrib.auth.forms import UserCreateionForm

class fooditemForm(ModelFrom):
    class Meta:
        model=Fooditem
        fields="__all__"

class addUserFooditem(ModelForm):
    class Meta:
        model=UserFooditem
        fields="__all__"

class createUserForm(UserCreateionForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']