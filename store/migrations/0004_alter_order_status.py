# Generated by Django 5.0.1 on 2024-05-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_order_orderitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('cod', 'cod'), ('online', 'online')], default='cod', max_length=200),
        ),
    ]
