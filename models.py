from django.db import models
from django.contrib.auth.models import User

from django import forms

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    name_of_enterprise = models.CharField(max_length=50)
    merchandise = models.CharField(max_length=50)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('name_of_enterprise','merchandise')

    
    

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
