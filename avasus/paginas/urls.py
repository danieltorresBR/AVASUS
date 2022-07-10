from django.urls import path
from .views import IndexView,  LoginView, DashboardView, SobreView, AjudaView
from .views import UsuarioCreate


urlpatterns = [
    # path('endereco/', MinhaView.as_view(), name='inicio')
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('ajuda/', AjudaView.as_view(), name='ajuda'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
]