# Generated by Django 2.1 on 2020-06-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0007_product_date_w'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_w',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]