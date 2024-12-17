from django.urls import path
from .views import*

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    path('categoria/', listagem_categoria, name='listagem_categoria'),
    path('categoria/cadastro', cadastrar_categoria, name='cadastro_categoria'),
    path('categoria/editar/<int:id>', editar_categoria, name='editar_categoria'),
    path('categoria/excluir/<int:id>', deletar_categoria, name='deletar_categoria'),
    # Add your URL patterns here
]