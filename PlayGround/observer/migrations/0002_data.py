# Generated by Django 3.2.6 on 2021-08-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('sub_subject', models.CharField(max_length=50)),
                ('template', models.CharField(max_length=500)),
            ],
        ),
    ]
