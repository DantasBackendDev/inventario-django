from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.cadastrar_produto, name='cadastrar_produto'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
]