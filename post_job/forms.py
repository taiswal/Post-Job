from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'company_name',
            'job_type',
            'location',
            'skill_tag',
            'salary',
            'industry',
            'experience_level',
            'work_environment',
            'description',
            'user',
            'image',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Location'}),
            'skill_tag': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'salary': forms.Select(attrs={'class': 'form-select'}),
            'industry': forms.Select(attrs={'class': 'form-select'}),
            'experience_level': forms.Select(attrs={'class': 'form-select'}),
            'work_environment': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe the job...'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name']
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'user']

        
