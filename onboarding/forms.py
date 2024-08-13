from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from .models import Company, Builder, CompanyMember
# Company Form
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email', 'phone_number', 'address', 'logo', 'registration_document', 'website']

# Builder Form
class BuilderForm(forms.ModelForm):
    class Meta:
        model = Builder
        fields = ['company', 'name', 'email', 'phone_number', 'profile_picture']
class CompanyMemberForm(forms.ModelForm):
    class Meta:
        model = CompanyMember
        fields = ['user', 'company', 'role']

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(validators=[EmailValidator()], required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    age = forms.IntegerField(required=True)
    address = forms.CharField(max_length=50, required=True)
    city = forms.CharField(max_length=30, required=True)
    state = forms.CharField(max_length=30, required=True)
    zipcode = forms.CharField(max_length=10, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18:
            raise ValidationError(_('You must be at least 18 years old to register.'))
        return age

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError(_("Passwords do not match."))
