from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'quantidade_estoque', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nome',)