# Generated by Django 4.2.7 on 2023-11-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eBhandar', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Vegetable', 'Vegetable'), ('Fruits', 'Fruits'), ('Electronics', 'Electronics'), ('Daily Needs', 'Daily Needs'), ('Medicine', 'Medicine'), ('Dry Fruits', 'Dry Fruits'), ('Stationary', 'Stationary')], default='Category', max_length=50),
        ),
    ]