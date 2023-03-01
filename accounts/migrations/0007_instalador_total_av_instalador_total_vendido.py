# Generated by Django 4.1.6 on 2023-02-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_instalador_divida'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalador',
            name='total_av',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instalador',
            name='total_vendido',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]