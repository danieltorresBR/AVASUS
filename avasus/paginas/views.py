from multiprocessing import context
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404

from .forms import UsuarioForm

# Create your views here.

class IndexView(TemplateView):
    template_name = "paginas/index.html"
class LoginView(TemplateView):
    template_name = "paginas/login.html"

class DashboardView(TemplateView):
    template_name = "paginas/dashboard.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"

class AjudaView(TemplateView):
    template_name = "paginas/ajuda.html"

class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Discente")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context