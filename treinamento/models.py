from django.db import models
from django.core.validators import RegexValidator


class Curso(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    nome = models.CharField(max_length=100, verbose_name="Nome")
    photo = models.ImageField(upload_to='curso/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Instrutor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    cpf = models.CharField(max_length=14, unique=True)
    date_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(max_length=150, verbose_name="Email")

    def __str__(self):
        return self.name

class Aluno(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    cpf = models.CharField(max_length=14, unique=True)    
    telefone = models.CharField(max_length=17, unique=True, verbose_name="Telefone")
    email = models.EmailField(max_length=150, verbose_name="Email")
    date_nasc = models.DateField(verbose_name="Data de Nascimento")
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='alunos', verbose_name="Curso")
    instrutor = models.ForeignKey(Instrutor, on_delete=models.PROTECT, related_name='alunos', verbose_name="Instrutor")

    def __str__(self):
        return self.name

class QuantAluno(models.Model):
    alunos_count = models.IntegerField()
    cursos_count = models.IntegerField()  
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Curso: {self.curso.nome} Alunos: {self.alunos_count}'
