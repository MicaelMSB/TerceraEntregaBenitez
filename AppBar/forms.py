from django import forms
from .models import Avatar



class AvatarFormulario(forms.ModelForm):
    class Meta:
        model=Avatar
        fields=('imagen',)
