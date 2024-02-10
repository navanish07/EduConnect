from django.forms import  ModelForm 
from .models import Room

# A ModelForm is a class that allows you to create a form from a model.

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']