from django import forms
from PaddeApp.models import FavoriteTurtle, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('favorite_turtle_name', 'profileinfo')

class FavoriteTurtleForm(forms.ModelForm):

    class Meta:
        model = FavoriteTurtle
        fields = ('title', 'turtleinfo')

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
            )

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user