# Generated by Django 4.1.6 on 2023-02-22 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_instalador_total_av_instalador_total_vendido'),
        ('falcao', '0004_alter_produtos_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendas',
            name='instalador',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.instalador'),
            preserve_default=False,
        ),
    ]
