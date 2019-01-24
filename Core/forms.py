# from django import forms
# from .models import Chamado, Area, Problema
# import json
from django.contrib.auth.models import User
from django.forms import *
from Core.models import Chamado, Problema, Area, Categoria_Problema
from Core.widget import TableSelect


class ChamadoCreateForm(ModelForm):

    class Meta:

        model = Chamado
        fields = '__all__'
        widgets = {
            'categoria_problema': RadioSelect(attrs={'class': 'center'}),
            'desc_problema': Textarea(attrs={'class': 'materialize-textarea'}),
             #Field ocultada, a mesma será inicializada na view sem visão ao usuário
            'criador': HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.fields['problema'].queryset = Problema.objects.none()        # Inicializa o Form vazio
        if 'area' in self.data: 
            try:
                area_id = int(self.data.get('area'))
                self.fields['problema'].queryset = Problema.objects.filter(
                    area_id=area_id).order_by('desc_problema')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['problema'].queryset = self.instance.area.problema_set.order_by('desc_problema')

        self.fields['categoria_problema'].queryset = Categoria_Problema.objects.none() # Inicializa o Form vazio

        if 'problema' in self.data:
            try:
                problema_id = int(self.data.get('problema'))
                self.fields['categoria_problema'].queryset = Categoria_Problema.objects.filter(problema_id=problema_id).order_by('desc_categoria_problema')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['categoria_problema'].queryset = self.instance.problema.categoria_problema_set.order_by('desc_categoria_problema')

class ChamadoUpdateForm(ModelForm):
    
    class Meta:
        model = Chamado
        fields = '__all__'
        widgets = {
            'categoria_problema': RadioSelect(attrs={'class': 'center'}),
            'desc_problema': Textarea(attrs={'class': 'materialize-textarea'}),
             #Field ocultada, a mesma será inicializada na view sem visão ao usuário
            'criador': HiddenInput(),
        }

class ChamadoCloseForm(ModelForm):
    
    class Meta:
        model = Chamado
        fields = '__all__'

class ChamadoDetailForm(ModelForm):
    
    class Meta:
        model = Chamado
        fields = '__all__'
