from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.

def contact_us_page(request):
    if request.method == "POST":
        return redirect(reverse("home_page"))
    return render(request, 'contact_module/contact_us_page.html')

