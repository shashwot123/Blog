from django import forms
from .models import Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["text"]
        widgets = {
            "text": forms.TextInput(attrs={
                "class": "comment-text",
                "placeholder": "Enter your comment...",
            }),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {
            "username" : "",
            "password1" : "",
            "password2" : "",
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Completely remove password field help_texts added by validators
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''
