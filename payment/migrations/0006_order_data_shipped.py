# Generated by Django 5.1.1 on 2024-10-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_order_shipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='data_shipped',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
