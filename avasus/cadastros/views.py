from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Modulo, Curso, Atividade
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin


# Create your views here.
class ModuloCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Modulo
    fields = ['nome', 'descricao', 'objetivo', 'idade_minima']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modulos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de novo módulo"
        context['botao'] = "Cadastrar"

        return context



class CursoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Curso
    fields = ['nome', 'carga_horaria', 'ordem', 'modulo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cursos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de novo curso"
        context['botao'] = "Cadastrar"

        return context

class AtividadeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Atividade
    fields = ['status', 'upload', 'curso']
    template_name = 'cadastros/form-upload.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de nova tarefa"
        context['botao'] = "Cadastrar"

        return context

#######UPDATE#######
class ModuloUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Modulo
    fields = ['nome', 'descricao', 'objetivo', 'idade_minima']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-modulos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Edição de módulo"
        context['botao'] = "Salvar"

        return context

class CursoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Curso
    fields = ['nome', 'carga_horaria', 'ordem', 'modulo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cursos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Edição de curso"
        context['botao'] = "Salvar"

        return context

class AtividadeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Atividade
    fields = ['status', 'upload', 'curso']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Edição de tarefa"
        context['botao'] = "Salvar"

        return context

#######DELETE#######
class ModuloDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Modulo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-modulos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir módulo"
        context['botao'] = "Confirmar"

        return context

class CursoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Curso
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cursos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir curso"
        context['botao'] = "Confirmar"

        return context

class AtividadeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir tarefa"
        context['botao'] = "Confirmar"

        return context


#######LIST#######
class ModuloList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Modulo
    template_name = 'cadastros/listas/modulo.html'


class CursoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Curso
    template_name = 'cadastros/listas/curso.html'

class AtividadeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'

