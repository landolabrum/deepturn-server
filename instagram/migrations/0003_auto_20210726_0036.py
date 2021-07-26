# Generated by Django 3.2.5 on 2021-07-26 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20210726_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cookies',
            name='id',
        ),
        migrations.AlterField(
            model_name='cookies',
            name='account',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='instagram.account'),
            preserve_default=False,
        ),
    ]
