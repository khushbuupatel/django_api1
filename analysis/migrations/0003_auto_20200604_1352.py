# Generated by Django 2.1 on 2020-06-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20200603_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=1),
        ),
    ]
