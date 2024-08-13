from django.contrib.auth.models import User
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    logo = models.ImageField(upload_to='company_logos/')
    registration_document = models.FileField(upload_to='registration_documents/')
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Role(models.Model):
    ROLE_CHOICES = [
        ('MD', 'Managing Director'),
        ('Manager', 'Manager'),
        ('Employee', 'Employee'),
        ('Associate', 'Associate'),
    ]
    name = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

class CompanyMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.role.name} at {self.company.name}"

class Builder(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='builder_profiles/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
