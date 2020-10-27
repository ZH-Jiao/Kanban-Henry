from django.db import models
from djongo import models
from django import forms
# Create your models here.


class Comment(models.Model):
    author = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        abstract = True


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'author', 'content'
        )


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    education = models.TextField()
    contact = models.IntegerField()
    status = models.CharField(max_length=200)
    rate = models.FloatField()
    rate_number = models.IntegerField()
    comment = models.ArrayField(model_container=Comment, model_form_class=CommentForm, default=list)



