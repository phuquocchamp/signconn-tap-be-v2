from django.db import models


class Profiles(models.Model):
    name = models.CharField(max_length=225)
    slogan = models.CharField(max_length=225)
    img = models.CharField(max_length=225)  # save only file name
    contact = models.JSONField(default=list)
    def __str__(self):
        return self.name


# class Contacts(models.Model):
#     profile = models.ForeignKey(Profiles, related_name='contacts', on_delete=models.CASCADE)
#     name = models.CharField(max_length=225)
#     link = models.URLField()

#     def __str__(self):
#         return self.name
