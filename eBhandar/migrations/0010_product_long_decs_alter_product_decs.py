# Generated by Django 4.2.7 on 2023-11-19 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eBhandar', '0009_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='long_decs',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='decs',
            field=models.CharField(max_length=50),
        ),
    ]