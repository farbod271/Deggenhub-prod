from django import forms
from django.forms import ModelForm
from .models import Task, Event
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser




class CustomSignupForm(UserCreationForm):
    user = get_user_model()
    custom_user_type = forms.ChoiceField(choices=user.USER_TYPE_CHOICES)
    profile_picture = forms.ImageField( required=False)
    class Meta:
        model = get_user_model()
        fields = ['username'  , 'email', 'custom_user_type', 'profile_picture']

class ProfileForm(ModelForm):
	class Meta:
		model = get_user_model()
		fields = ['username'  , 'email', 'profile_picture', 'first_name', 'last_name']
 
          



class TaskForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=50)
    task_type = forms.ChoiceField(choices=Task.TASK_TYPE_CHOICES)
    description = forms.CharField(widget=forms.Textarea, max_length=500)
    class Meta:
        model = Task
        fields = ['title', 'task_type', 'description', 'image', 'contact_info', 'task_eco', 'price']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'task_type': forms.Select(choices=Task.TASK_TYPE_CHOICES, attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        # }

class EventForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    occurance = forms.DateTimeField()
    class Meta:
        model = Event
        fields = ['title', 'description', 'occurance', 'image', 'place']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control input-box'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(),
            'occurance': forms.DateTimeInput(attrs={'class': 'form-control'})
        }


    