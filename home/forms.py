from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):

    TUTORING_PACKAGES = [
        ('', 'Select a package...'),
        ('package1', 'Package 1'),
        ('package2', 'Package 2'),
        ('package3', 'Package 3'),
        # Add more packages as needed...
    ]

    tutoring_package = forms.ChoiceField(choices=TUTORING_PACKAGES, widget=forms.Select(attrs={'placeholder': 'Choose your preferred tutoring package.'}))
    service_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Describe the service you\'re looking for.', 'rows': 5}))
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your full name.'}))
    customer_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address.'}))
    customer_phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number.'}))

    class Meta:
        model = Application
        fields = ['tutoring_package', 'service_description', 'customer_name', 'customer_email', 'customer_phone']