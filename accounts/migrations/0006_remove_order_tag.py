# Generated by Django 4.1.4 on 2023-01-02 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_product_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
    ]
