# Generated by Django 3.0.8 on 2020-07-25 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alumno'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='cursos',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='web.Curso'),
        ),
    ]
