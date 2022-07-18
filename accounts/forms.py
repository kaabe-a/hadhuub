from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from . models import Profile, Social, User

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name')

class ProfileForm(forms.ModelForm):
    dateOfBirth = forms.DateField(widget=forms.TextInput(
        attrs = {'type':'date'}
    	))
    class Meta:
        model = Profile
        fields = ('dateOfBirth','phone','bio','profile','cover')

class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ('website','linkedin','facebook','twitter','github')