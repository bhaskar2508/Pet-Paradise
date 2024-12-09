# Generated by Django 5.0.7 on 2024-12-01 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=600)),
                ('image', models.ImageField(default='', upload_to='image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petapp.catgory')),
            ],
            options={
                'db_table': 'CatFood',
            },
        ),
    ]