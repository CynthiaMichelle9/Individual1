# Generated by Django 4.2.2 on 2023-07-02 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_prioridad'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='prioridad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.prioridad'),
        ),
    ]