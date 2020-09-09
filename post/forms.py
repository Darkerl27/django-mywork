from django import  forms
from .models import News,Category,Comment


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields = ('title', 'content', 'category', 'is_published', 'photo')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),

        }

class UserAddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'body', )
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),


        }

class UpdateNewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields = ('title', 'content', 'category', 'is_published', 'photo')

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),

        }