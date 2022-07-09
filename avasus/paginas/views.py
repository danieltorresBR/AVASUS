from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.
class IndexView(TemplateView):
    template_name = "paginas/modelo.html"

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"

class LoginView(TemplateView):
    template_name = "paginas/login.html"

