# Generated by Django 3.0.5 on 2020-04-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default=True, max_length=5000),
        ),
    ]