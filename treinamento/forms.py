from django import forms
from .models import Aluno, Curso

class NewAlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['curso'].queryset = Curso.objects.all()

class NovoCursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'