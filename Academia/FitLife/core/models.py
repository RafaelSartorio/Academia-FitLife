from django.db import models
from django.contrib.auth.models import User

class Aulas(models.Model):
    nomeAula = models.CharField(max_length=30 , verbose_name='Nome da aula')
    descricao = models.TextField(verbose_name='Descrição da aula', blank=True, null=True)
    data_aula= models.DateTimeField(verbose_name='Data e hora da aula')
    aluno= models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table='Aulas'
    
    def __str__(self):
        return self.nomeAula
    
    def data_evento_criacao(self):
        return self.data_aula.strftime('%d/%m/%Y as %H:%M hrs')
    
# class user(models.Model):
#     User = models.CharField(max_length=30, verbose_name='usuario')
#     password = models.TextField(verbose_name='senha')
#     email = models.TextField(verbose_name='email')
    

