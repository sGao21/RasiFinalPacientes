# Generated by Django 3.2.6 on 2023-12-05 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notas', models.TextField()),
                ('historia_clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionPacientes.historiaclinica')),
            ],
        ),
    ]
