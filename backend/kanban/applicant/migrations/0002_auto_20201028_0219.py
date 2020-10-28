# Generated by Django 2.2.7 on 2020-10-28 02:19

import applicant.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='comment',
            field=djongo.models.fields.ArrayField(default=list, model_container=applicant.models.Comment, model_form_class=applicant.models.CommentForm),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='rate',
            field=models.FloatField(),
        ),
    ]