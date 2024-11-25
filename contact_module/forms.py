from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        max_length = 50,
        label = "نام و نام خانوادگی",
        error_messages = {
            'required' : "لطفاَ نام و نام خانوادگی را وارد کنید",
            'max_length' : "نام و نام خانوادگی نمی تواند بیشتر از 50 کاراکتر باشد"
        },
        widget = forms.TextInput(attrs = {
            'class' : 'form-control',
            'placeholder' : 'نام و نام خانوادگی'
        })
    )
    email = forms.EmailField(
        label = "ایمیل",
        widget = forms.EmailInput(attrs ={
            'class' : 'form-control',
            'placeholder' : 'ایمیل'
        })
    )
    subject = forms.CharField(
        label = "عنوان",
        widget = forms.TextInput(attrs = {
            'class' : 'form-control',
            'placeholder' : 'عنوان'
        })
    )
    text = forms.CharField(
        label = "متن پیام",
        widget = forms.Textarea(attrs = {
            'class' : 'form-control',
            'placeholder' : 'متن خود را بنویسید...',
            'id' : 'message'
        })
    )
