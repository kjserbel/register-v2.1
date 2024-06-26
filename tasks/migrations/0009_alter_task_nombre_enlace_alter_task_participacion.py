# Generated by Django 5.0.3 on 2024-03-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_rename_questionone_task_c_p_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='nombre_enlace',
            field=models.CharField(choices=[('Vasti Arana', 'Vasti Arana'), ('Israel', 'Isrrael'), ('Omar Castellanos', 'Omar Castellanos'), ('Esther Castellanos', 'Esther Castellanos')], max_length=250),
        ),
        migrations.AlterField(
            model_name='task',
            name='participacion',
            field=models.CharField(choices=[('RC', 'Representante de Casilla'), ('RG', 'Representante General'), ('MV', 'Movilizador'), ('SP', 'Simpatizante')], max_length=100),
        ),
    ]
