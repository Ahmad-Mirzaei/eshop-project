from django import forms
from django.core.exceptions import ValidationError
from setuptools.config.pyprojecttoml import validate
from django.core.validators import MaxLengthValidator, MinLengthValidator
from account_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address', 'about_user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            })
        }

        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'avatar': 'تصویر پروفایل',
            'address': 'آدرس',
            'about_user': 'درباره من',
        }


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                       label="کلمه عبور فعلی",
                                       validators=[MaxLengthValidator(100)]
                                       )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                               label="کلمه عبور جدید",
                               validators=[MaxLengthValidator(100)]
                               )
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
                                       label="تکرار کلمه عبور جدید",
                                       validators=[MaxLengthValidator(100)]
                                       )

    def clean_confirm_new_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        raise ValidationError('کاربر گرامی، کلمه ی عبور و تکرار آن مغایرت دارند؛ لطفاً دوباره سعی کنید.')