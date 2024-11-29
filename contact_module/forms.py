from django import forms
from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        # fields = '__all__'
        # exclude = ['response']
        widgets = {
            'full_name' : forms.TextInput(attrs = {
                'class' : 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.TextInput(attrs={
                'class': 'form-control',
                'rows' : 5,
                'id' : 'message'
            })
        }

        labels = {
            'full_name' : 'نام و نام خانوادگی شما',
            'email' : 'ایمیل شما'
        }

        error_messages = {
            'full_name' : {
                'required' : 'کاربر گرامی، وارد کردن نام و نام خانوادگی الزامی است'
            },
        }


# class ProfileForm(forms.Form):
#     # user_image = forms.FileField(label = "تصویر کاربر")
#     user_image = forms.ImageField(label = "تصویر کاربر")
