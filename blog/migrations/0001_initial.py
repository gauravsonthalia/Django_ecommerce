# Generated by Django 3.0.5 on 2020-04-17 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('head0', models.CharField(default=True, max_length=500)),
                ('head1', models.CharField(default=True, max_length=500)),
                ('head2', models.CharField(default=True, max_length=500)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]