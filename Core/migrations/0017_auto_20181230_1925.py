# Generated by Django 2.1.3 on 2018-12-30 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0016_auto_20181230_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='status_chamado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Status_Chamado', verbose_name='Status'),
        ),
    ]
