from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # описываем поля которые будем заполнятьв форме
        fields = ['name',"lang","code"]
        labels = {"name":"","lang":"","code":""}
        widgets = {
            "name": TextInput(attrs={'placeholder': "Название сниппета"}),
            "code":Textarea(attrs={'placeholder': "Код сниппета"})
        }