from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'quantidade_estoque', 'categoria']
        labels = {
            'nome': 'Nome do produto',
            'preco': 'Preço',
            'quantidade_estoque': 'Quantidade em estoque',
            'categoria': 'Categoria',
        }