# Generated by Django 2.2 on 2020-06-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_auto_20200608_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='landline',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]