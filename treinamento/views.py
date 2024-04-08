from django.views.generic import TemplateView, CreateView,DetailView, DeleteView, UpdateView, ListView
from treinamento.models import Aluno, Curso
from treinamento.forms import NewAlunoForm, NovoCursoForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.db.models import Count

@method_decorator(login_required(login_url='login'), name='dispatch')
class HomeView(ListView):
    template_name = 'home.html'
    model = Curso
    context_object_name = 'cursos'


    def get_queryset(self):
        queryset = super().get_queryset().order_by('nome')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(nome__icontains=search)
        return queryset

@method_decorator(login_required(login_url='login'), name='dispatch')
class CursoDetailView(DetailView):
    model = Curso
    template_name = 'curso_detail.html'
    context_object_name = 'curso'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curso = self.object
        context['alunos'] = Aluno.objects.filter(curso=curso)
        return context

@method_decorator(login_required(login_url='login'),name='dispatch')
class NewAlunoView(CreateView):
    model = Aluno
    form_class = NewAlunoForm
    template_name = 'new_aluno.html'
    success_url = '/home/'
    
@method_decorator(login_required(login_url='login'),name='dispatch')
class NovoCursoView(CreateView):
    model = Curso
    form_class = NovoCursoForm
    template_name = 'novo_curso.html'
    success_url = '/home/'  

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

@method_decorator(login_required(login_url='login'),name='dispatch')
class UpdateAlunoView(UpdateView):
    model = Aluno
    form_class = NewAlunoForm
    template_name = 'aluno_update.html'


    def get_success_url(self):
        curso = self.object.curso
        return reverse_lazy('curso_detail',kwargs={'pk':curso.pk})

@method_decorator(login_required(login_url='login'),name='dispatch')
class DeleteAlunoView(DeleteView):
    model = Aluno    
    template_name = 'aluno_delete.html'
    success_url = '/home/'

@method_decorator(login_required(login_url='login'),name='dispatch')
class UpdateCursoView(UpdateView):
    model = Curso
    form_class = NovoCursoForm
    template_name = 'curso_update.html'


    def get_success_url(self):
        return reverse_lazy('curso_detail',kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'),name='dispatch')
class DeleteCursoView(DeleteView):
    model = Curso    
    template_name = 'curso_delete.html'
    success_url = '/home/'

class AlunosPorCursoListView(ListView):
    model = Curso
    template_name = 'alunos_por_curso.html'  # Nome do template onde os resultados serão exibidos
    context_object_name = 'cursos'

    def get_queryset(self):
        # Obtém todos os cursos juntamente com a contagem de alunos para cada curso
        cursos_com_alunos = Curso.objects.annotate(numero_alunos=Count('aluno'))
        return cursos_com_alunos