from django import forms
from django.contrib.auth import get_user_model

from .models import Note, Comment

User = get_user_model()


class NoteCreateForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'composer', 'description', 'pdf', 'image', 'pub_date')
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }