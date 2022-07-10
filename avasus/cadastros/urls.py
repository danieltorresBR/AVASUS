from django.urls import path
from .views import ModuloCreate, CursoCreate, AtividadeCreate
from .views import ModuloUpdate, CursoUpdate, AtividadeUpdate
from .views import ModuloDelete, CursoDelete, AtividadeDelete
from .views import ModuloList, CursoList, AtividadeList





urlpatterns = [
    # path('endereco/', MinhaView.as_view(), name='inicio')
    path('cadastrar/modulo/', ModuloCreate.as_view(), name='cadastrar-modulo'),
    path('cadastrar/curso/', CursoCreate.as_view(), name='cadastrar-curso'),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name='cadastrar-atividade'),
    
    path('editar/modulo/<int:pk>', ModuloUpdate.as_view(), name='editar-modulo'),
    path('editar/curso/<int:pk>', CursoUpdate.as_view(), name='editar-curso'),
    path('editar/atividade/<int:pk>', AtividadeUpdate.as_view(), name='editar-atividade'),

    path('excluir/modulo/<int:pk>', ModuloDelete.as_view(), name='excluir-modulo'),
    path('excluir/curso/<int:pk>', CursoDelete.as_view(), name='excluir-curso'),
    path('excluir/atividade/<int:pk>', AtividadeDelete.as_view(), name='excluir-atividade'),

    path('listar/modulos/', ModuloList.as_view(), name='listar-modulos'),
    path('listar/cursos/', CursoList.as_view(), name='listar-cursos'),
    path('listar/atividades/', AtividadeList.as_view(), name='listar-atividades'),

]