from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from treinamento.views import NewAlunoView, HomeView, CursoDetailView, NovoCursoView, UpdateAlunoView, DeleteAlunoView, UpdateCursoView, DeleteCursoView, AlunosPorCursoListView
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', HomeView.as_view(), name='home'),   
    path('novo_curso/', NovoCursoView.as_view(), name='novo_curso'), 
    path('new_aluno/', NewAlunoView.as_view(), name='new_aluno'),   
    path('curso/<int:pk>/', CursoDetailView.as_view(), name='curso_detail'), 
    path('aluno/<int:pk>/update', UpdateAlunoView.as_view(), name='aluno_update'), 
    path('aluno/<int:pk>/delete', DeleteAlunoView.as_view(), name='aluno_delete'), 
    path('curso/<int:pk>/update', UpdateCursoView.as_view(), name='curso_update'), 
    path('curso/<int:pk>/delete', DeleteCursoView.as_view(), name='curso_delete'), 
    path('alunos_por_curso/', AlunosPorCursoListView.as_view(), name='alunos_por_curso'),
    
        
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)