# Generated by Django 3.2.18 on 2023-02-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0006_faker_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='enqury',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('phonenumber', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=300)),
            ],
        ),
    ]
