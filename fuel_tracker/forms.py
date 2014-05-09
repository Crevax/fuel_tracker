from django import forms
from django.contrib.auth.models import User
from fuel_tracker.models import *

class VehicleForm(forms.ModelForm):
    nickname        = forms.CharField(max_length=100, help_text="Car Name:")
    make            = forms.CharField(max_length=50, help_text="Make:")
    model           = forms.CharField(max_length=50, help_text="Model:")
    year            = forms.CharField(max_length=4, help_text="Year:")
    base_miles      = forms.DecimalField(decimal_places=1, max_digits=7, help_text="Base Miles:")

    class Meta:
        model = Vehicle

class GasCompanyForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Company Name:")

    class Meta:
        model = GasCompany

class GasStationForm(forms.ModelForm):
    company         = forms.ModelChoiceField(queryset=GasCompany.objects.all(), help_text="Company: ")
    street_address  = forms.CharField(max_length=100, help_text="Street:")
    city            = forms.CharField(max_length=100, help_text="City:")
    state           = forms.CharField(max_length=50, help_text="State:")
    zipcode         = forms.CharField(max_length=5, help_text="Zipcode:")

    class Meta:
        model = GasStation

class FuelUpForm(forms.ModelForm):
    station             = forms.ModelChoiceField(queryset=GasStation.objects.all(), help_text="Company: ")
    vehicle             = forms.ModelChoiceField(queryset=Vehicle.objects.all(), help_text="Vehicle: ")
    gas_type            = forms.CharField(max_length=50, help_text="Gas Type: ", initial="Regular Unleaded")
    price_per_gallon    = forms.DecimalField(decimal_places=3, max_digits=4, help_text="Price Per Gallon: ")
    amount              = forms.DecimalField(decimal_places=3, max_digits=5, help_text="Amount: ")
    miles_traveled      = forms.DecimalField(decimal_places=1, max_digits=4, help_text="Miles Traveled: ")
    date                = forms.DateField(help_text="Date: ")

    class Meta:
        model = FuelUp

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'avatar')