# Generated by Django 3.0.5 on 2020-05-17 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libra', '0019_auto_20200517_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]
