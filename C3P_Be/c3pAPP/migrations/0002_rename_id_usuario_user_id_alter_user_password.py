# Generated by Django 4.1.1 on 2022-09-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c3pAPP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_usuario',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256, verbose_name='Password'),
        ),
    ]