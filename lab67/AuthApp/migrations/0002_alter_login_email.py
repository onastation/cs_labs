# Generated by Django 4.0.5 on 2022-06-17 14:24

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('AuthApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=10)),
        ),
    ]
