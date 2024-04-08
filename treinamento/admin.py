from django.contrib import admin
from .models import Aluno, Instrutor, Curso

class CadAluno(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'telefone', 'email', 'curso', 'get_instrutor_name')

    def get_instrutor_name(self, obj):
        return obj.instrutor.name if obj.instrutor else ""
    get_instrutor_name.short_description = 'Instrutor'

class CadInstrutor(admin.ModelAdmin):
    list_display = ('id', 'name', 'cpf', 'email')

class CadCurso(admin.ModelAdmin):
    list_display = ('id','nome',)

admin.site.register(Aluno, CadAluno)
admin.site.register(Curso, CadCurso)
admin.site.register(Instrutor, CadInstrutor)  # Registrar o modelo Instrutor com o ModelAdmin personalizado

