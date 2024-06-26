# Generated by Django 5.0.6 on 2024-06-17 13:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aulas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeAula', models.CharField(max_length=30, verbose_name='Nome da aula')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição da aula')),
                ('data_aula', models.DateTimeField(verbose_name='Data e hora da aula')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Aulas',
            },
        ),
    ]
