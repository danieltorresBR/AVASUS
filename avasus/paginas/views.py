from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

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
