# Generated by Django 2.2.3 on 2019-08-09 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='ticket_amount_5',
        ),
        migrations.RemoveField(
            model_name='post',
            name='ticket_date_5',
        ),
        migrations.RemoveField(
            model_name='post',
            name='ticket_price_5',
        ),
    ]