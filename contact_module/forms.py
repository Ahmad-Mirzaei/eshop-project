from django import forms


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        max_length = 50,
        error_messages = {
            "required" : "لطفاَ نام و نام خانوادگی را وارد کنید"
        },
        label = "نام و نام خانوادگی")
    email = forms.EmailField(widget = forms.EmailInput, label = "ایمیل")
    subject = forms.CharField(label = "عنوان")
    text = forms.CharField(widget = forms.Textarea, label = "متن پیام")
