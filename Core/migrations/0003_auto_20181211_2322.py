# Generated by Django 2.1.3 on 2018-12-11 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_auto_20181211_1937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chamado',
            options={'ordering': ['-id'], 'verbose_name': 'Chamado', 'verbose_name_plural': 'Chamados'},
        ),
    ]