from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from django.db import DatabaseError
from .models import Produto, Categoria
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def lista_produtos(request):
    produtos = Produto.objects.select_related('categoria').all()
    contexto = {'produtos': produtos}
    return render(request, 'inventario/lista_produtos.html', contexto)

@login_required
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

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.annotate(total_produtos=Count('produtos')).order_by('id')
    contexto = {'categorias': categorias}
    return render(request, 'inventario/lista_categorias.html', contexto)

@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            try:
                form.save()
                return redirect('inventario:lista_produtos')
            except DatabaseError:
                form.add_error(None, 'Erro ao salvar no banco. Tente novamente.')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'inventario/form_produto.html', {'form': form, 'produto': produto})


@login_required
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        try:
            produto.delete()
            return redirect('inventario:lista_produtos')
        except DatabaseError:
            return render(request, 'inventario/confirmar_delecao.html', {
                'produto': produto,
                'erro': 'Erro ao deletar. Tente novamente.'
            })

    return render(request, 'inventario/confirmar_delecao.html', {'produto': produto})   
