# Generated by Django 2.2.3 on 2019-08-14 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190814_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='t_choice',
            field=models.CharField(choices=[('ticket1', 'c1'), ('ticket2', 'c2'), ('ticket2', 'c3'), ('ticket2', 'c4')], default='ticket1', max_length=100),
        ),
    ]
