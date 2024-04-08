from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Aluno, Curso, QuantAluno
from django.db.models import Count


def update_quant_aluno():
    cursos_count = Curso.objects.all().count()
    alunos_count = Aluno.objects.all().count()
    Curso.objects.annotate(quant_alunos=Count("alunos"))
    QuantAluno.objects.create(
        alunos_count=alunos_count,
        cursos_count=cursos_count
    )

@receiver(post_save, sender=Aluno)
def aluno_post_save(sender, instance, **kwargs):
    update_quant_aluno()

@receiver(post_delete, sender=Aluno)
def aluno_post_delete(sender, instance, **kwargs):
    update_quant_aluno()

@receiver(post_save, sender=Curso)
def curso_post_save(sender, instance, **kwargs):
    update_quant_aluno()

@receiver(post_delete, sender=Curso)
def curso_post_delete(sender, instance, **kwargs):
    update_quant_aluno()

