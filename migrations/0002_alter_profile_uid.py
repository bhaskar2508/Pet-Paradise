# Generated by Django 5.0.7 on 2024-11-11 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x000001796F0C79C0>', max_length=200),
        ),
    ]