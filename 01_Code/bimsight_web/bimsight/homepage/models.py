from django.db import models

class loginInfo(models.Model):
    SEX_CHOICES = [{'M', 'Male'}, {'F', 'Female'}]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)