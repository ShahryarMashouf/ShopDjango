# Generated by Django 5.0.6 on 2024-07-13 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_cart_created_at_remove_cartitem_added_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=1000)),
            ],
        ),
    ]
