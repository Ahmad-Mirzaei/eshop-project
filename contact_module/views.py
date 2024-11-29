from django.shortcuts import render, redirect
from .forms import ContactUsModelForm
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from .models import ContactUs,UserProfile
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




def store_file(file):
    with open('temp/image.jpg', 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)


# step 1
# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, 'contact_module/create_profile_page.html', {'form' : form})
#
#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)
#         if submitted_form.is_valid():
#             # store_file(request.FILES['profile'])
#             profile = UserProfile(image = request.FILES["user_image"])
#             profile.save()
#             return redirect('/contact-us/create-profile')
#         return render(request, 'contact_module/create_profile_page.html', {'form': submitted_form})

# step 2
class CreateProfileView(CreateView):
    model = UserProfile
    template_name = 'contact_module/create_profile_page.html'
    fields = '__all__'
    success_url = '/contact-us/create-profile'


class ProfilesView(ListView):
    model = UserProfile
    template_name = 'contact_module/create_profile_page.html'
    context_object_name = 'profiles'