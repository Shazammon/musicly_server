# Generated by Django 4.1.2 on 2022-10-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
