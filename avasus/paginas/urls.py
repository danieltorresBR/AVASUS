from django.urls import path
from .views import IndexView, SobreView, LoginView


urlpatterns = [
    # path('endereco/', MinhaView.as_view(), name='inicio')
    path('', IndexView.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('login/', LoginView.as_view(), name='login'),
]