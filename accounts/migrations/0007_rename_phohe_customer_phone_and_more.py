# Generated by Django 4.1.4 on 2023-01-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_order_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phohe',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
