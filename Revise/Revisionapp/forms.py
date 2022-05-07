from django import forms
from django.core import validators
from Revisionapp.models import visitors, UserProfileInfo
from django.contrib.auth.models import User

class Form_visitors(forms.ModelForm):
    visitorname = forms.CharField()
    visitoremail = forms.EmailField()
    visitorage = forms.IntegerField(validators=[validators.MaxValueValidator(80),validators.MinValueValidator(18)])

    class Meta:
        model = visitors
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site',)
