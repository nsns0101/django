# Generated by Django 2.2.3 on 2020-01-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=30)),
                ('product_quantity', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('product_sale', models.IntegerField(default=0)),
                ('product_image', models.TextField()),
                ('product_area', models.TextField(default='Korea')),
                ('product_made', models.TextField()),
                ('product_created_at', models.DateTimeField(auto_now=True)),
                ('product_updated_at', models.DateTimeField(auto_now=True)),
                ('product_order_number', models.IntegerField(default=0)),
                ('product_seller', models.CharField(default='nsns0101', max_length=20)),
            ],
        ),
    ]
