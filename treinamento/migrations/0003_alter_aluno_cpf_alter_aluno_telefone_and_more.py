# Generated by Django 5.0.3 on 2024-04-05 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treinamento', '0002_remove_quantaluno_curso_remove_quantaluno_instrutor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(max_length=17, unique=True, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='instrutor',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
