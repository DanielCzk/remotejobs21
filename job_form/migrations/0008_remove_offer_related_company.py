# Generated by Django 3.1.6 on 2021-02-28 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_form', '0007_offer_related_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='related_company',
        ),
    ]