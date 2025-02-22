# Generated by Django 5.0.3 on 2024-04-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='product_images/')),
                ('description', models.TextField()),
            ],
        ),
    ]
