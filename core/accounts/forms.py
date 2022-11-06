from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label = 'رمز عبور',
        widget= forms.PasswordInput
    )
    password2 = forms.CharField(
        label = 'تکرار رمز عبور',
        widget= forms.PasswordInput
    )
    class Meta:
        model = User
        fields = ('email','full_name')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1']!=cd['password2'] :
            raise forms.ValidationError('پسوردها همخوانی ندارند')
        return cd['password1']

    def clean_password(self):
        cd = self.cleaned_data
        if len(cd['password1']) < 6 :
            raise forms.ValidationError('پسورد حداقل باید دارای 6 حرف باشد')
        return cd['password1']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit :
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name')

    def clean_password(self):
        return self.initial['password']
