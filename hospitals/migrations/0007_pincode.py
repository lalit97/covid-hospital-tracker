# Generated by Django 2.2 on 2020-06-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0006_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
