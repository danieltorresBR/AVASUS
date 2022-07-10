from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Modulo, Curso, Atividade
from django.urls import reverse_lazy

# Create your views here.
class ModuloCreate(CreateView):
    model = Modulo
    fields = ['nome', 'descricao', 'objetivo', 'idade_minima']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modulos')

class CursoCreate(CreateView):
    model = Curso
    fields = ['nome', 'carga_horaria', 'ordem', 'modulo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cursos')


class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['status', 'upload', 'curso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


#######UPDATE#######
class ModuloUpdate(UpdateView):
    model = Modulo
    fields = ['nome', 'descricao', 'objetivo', 'idade_minima']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modulos')

class CursoUpdate(UpdateView):
    model = Curso
    fields = ['nome', 'carga_horaria', 'ordem', 'modulo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cursos')


class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['status', 'upload', 'curso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

#######DELETE#######
class ModuloDelete(DeleteView):
    model = Modulo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modulos')

class CursoDelete(DeleteView):
    model = Curso
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cursos')


class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')

#######LIST#######
class ModuloList(ListView):
    model = Modulo
    template_name = 'cadastros/listas/modulo.html'

class CursoList(ListView):
    model = Curso
    template_name = 'cadastros/listas/curso.html'

class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'
