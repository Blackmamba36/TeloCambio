# Generated by Django 4.0.2 on 2022-02-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Te Lo Cambio', max_length=255),
        ),
    ]
