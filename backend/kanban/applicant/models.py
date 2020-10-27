from django.db import models
from djongo import models
# Create your models here.


class Comment(models.Model):
    author = models.CharField(max_length=200)
    content = models.TextField()


class Applicant(models.Model):
    name = models.TextField()
    education = models.TextField()
    contact = models.IntegerField()
    status = models.CharField(max_length=200)
    rate = models.IntegerField()
    rate_number = models.IntegerField()
    comment = models.ArrayField(model_container=Comment)


