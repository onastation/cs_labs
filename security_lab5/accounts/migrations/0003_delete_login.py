# Generated by Django 4.0.5 on 2022-06-17 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_login_delete_logins'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]