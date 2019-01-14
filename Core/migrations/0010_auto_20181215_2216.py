# Generated by Django 2.1.3 on 2018-12-15 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0009_auto_20181213_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status_chamado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Status_Chamado', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='status_chamado',
            name='status',
            field=models.CharField(max_length=150),
        ),
    ]