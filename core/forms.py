from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body',
        ]

class SearchForm(forms.Form):
    q = forms.CharField(label='search',max_length=50)