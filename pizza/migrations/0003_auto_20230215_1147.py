# Generated by Django 3.2.18 on 2023-02-15 06:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20230215_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('69e892d9-215b-4afb-88ae-eee79ff4d0e3'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cart_items',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('69e892d9-215b-4afb-88ae-eee79ff4d0e3'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='pizza_image',
            field=models.ImageField(upload_to='uploads\\products'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('69e892d9-215b-4afb-88ae-eee79ff4d0e3'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pizzacategory',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('69e892d9-215b-4afb-88ae-eee79ff4d0e3'), primary_key=True, serialize=False),
        ),
    ]
