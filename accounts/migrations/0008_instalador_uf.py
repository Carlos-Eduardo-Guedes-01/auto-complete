# Generated by Django 4.1.6 on 2023-02-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_instalador_total_av_instalador_total_vendido'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalador',
            name='uf',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
    ]
