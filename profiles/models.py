from django.db import models


# Create your models here.

class Profiles(models.Model):
    name = models.CharField(max_length=225)
    slogan = models.CharField(max_length=225)
    img = models.CharField(max_length=225)  # save only file name

    def __str__(self):
        return self.name


class Contact(models.Model):
    profile = models.ForeignKey(Profiles, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    link = models.URLField()

    def __str__(self):
        return f"{self.profile.name} - {self.name}"
