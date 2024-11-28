from django.shortcuts import render, redirect
from .forms import ContactUsModelForm
from django.views import View
from django.views.generic.edit import FormView, CreateView
from .models import ContactUs
# Create your views here.

# step 1 with get and post method
# class ContactUsView(View):
#     def get(self, request):
#         contact_form = ContactUsModelForm()
#         return render(request, 'contact_module/contact_us_page.html', {
#             'contact_form': contact_form
#         })
#     def post(self, request):
#         contact_form = ContactUsModelForm(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect('home_page')
#         return render(request, 'contact_module/contact_us_page.html', {
#             'contact_form': contact_form
#         })


# step 2 with FormView
# class ContactUsView(FormView):
#     template_name = 'contact_module/contact_us_page.html'
#     form_class = ContactUsModelForm
#     success_url = '/contact-us/'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# step 3 with CreateView
class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact-us/'



