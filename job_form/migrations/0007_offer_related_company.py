# Generated by Django 3.1.6 on 2021-02-28 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_company', '0005_auto_20210227_2148'),
        ('job_form', '0006_remove_offer_company_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='related_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related', to='job_company.company'),
        ),
    ]
