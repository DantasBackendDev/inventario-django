from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.db import DatabaseError
from .models import Produto, Categoria

# Create your views here.
def lista_produtos(request):
    produtos = Produto.objects.select_related('categoria').all()
    contexto = {'produtos': produtos}
    return render(request, 'inventario/lista_produtos.html', contexto)


def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('inventario:lista_produtos')
            except DatabaseError:
                form.add_error(None, 'Erro ao savar no banco. Tente novamente.')
    else:
        form = ProdutoForm()

    return render(request, 'inventario/form_produto.html', {'form': form})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    contexto = {'categorias': categorias}
    return render(request, 'inventario/lista_categorias.html', contexto)