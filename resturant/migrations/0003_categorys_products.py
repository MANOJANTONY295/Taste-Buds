# Generated by Django 4.2.5 on 2023-09-27 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0002_customuser_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('offer', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=30)),
                ('stock', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('on_discount', models.BooleanField(default=False)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturant.categorys')),
            ],
        ),
    ]
