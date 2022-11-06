from django import forms

class SearchEquipForm(forms.Form):
    search = forms.CharField(
        max_length=20 ,
        initial = '',
        widget = forms.TextInput(attrs={
            'class':'form-control',
        })
    )