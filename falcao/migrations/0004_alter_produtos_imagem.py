# Generated by Django 4.0.6 on 2023-02-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('falcao', '0003_alter_produtos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='imagem',
            field=models.ImageField(upload_to='falcao/media'),
        ),
    ]
