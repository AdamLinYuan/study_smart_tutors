from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import ApplicationForm, ContactForm
from django.core.mail import send_mail

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html')

# Tutoring Packages

def our_services(request):
  return render(request, 'tutoring/our-services.html')

def weekly_tutoring(request):
  return render(request, 'tutoring/weekly-tutoring.html')

def group_tutoring(request):
  return render(request, 'tutoring/group-tutoring.html')

def single_tutoring(request):
  return render(request, 'tutoring/single-tutoring.html')

def university_admissions(request): 
  return render(request, 'tutoring/university-admissions.html')

# Notes

def note1(request):
  return render(request, 'notes/note1.html')

# Help

def about(request):
  return render(request, 'help/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted successfully.')
            form_data = form.cleaned_data
            message = '\n'.join(f'{key}: {value}' for key, value in form_data.items())
            send_mail(
                'New Application Submitted',  # subject
                message,  # message
                'sstapplicationforms@gmail.com',  # from email
                ['adamyuanpersonal@gmail.com', 'adamtahri111@gmail.com'],  # to email
            )
            return redirect('contact-us')  # Redirect to a success page or another view
    else:
        form = ContactForm()
    return render(request, 'help/contact.html', {'form': form})

# Apply

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted successfully.')
            form_data = form.cleaned_data
            message = '\n'.join(f'{key}: {value}' for key, value in form_data.items())
            send_mail(
                'New Application Submitted',  # subject
                message,  # message
                'sstapplicationforms@gmail.com',  # from email
                ['adamyuanpersonal@gmail.com', 'adamtahri111@gmail.com'],  # to email
            )
            return redirect('apply')
    else:
        form = ApplicationForm()
    return render(request, 'apply/apply.html', {'form': form})

# Easter Egg

def beaubeau(request):
   return render(request, 'egg/beaubeau.html')


