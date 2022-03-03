# Generated by Django 4.0.2 on 2022-03-02 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('value', models.IntegerField()),
                ('product_type', models.CharField(choices=[('nuevo', 'nuevo'), ('usado', 'usado')], default='nuevo', max_length=10)),
                ('image', models.ImageField(default='default.jpg', upload_to='product')),
            ],
        ),
    ]