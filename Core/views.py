
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from django.contrib import messages
# from django.core import serializers
# import json

# from .models import Area, Problema, Categoria_Problema, Chamado
# from .forms import CriaChamado

################
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView
from .models import Chamado, Area, Problema, Categoria_Problema
from .forms import ChamadoForm



class HomeListView(ListView):

    model = Chamado
    context_object_name = 'chamado'
    paginate_by = 5


class ChamadoCreateView(SuccessMessageMixin, CreateView):

    model = Chamado
    form_class = ChamadoForm
    success_url = reverse_lazy('home')
    success_message = "Chamado was created successfully"

class ChamadoUpdateView(SuccessMessageMixin, UpdateView):
    model = Chamado
    form_class = ChamadoForm
    success_url = reverse_lazy('home')
    success_message = "Chamado was Updated successfully"

def content_details(request):

    if request.method == 'GET' and 'problema' in request.GET:

        area_id = request.GET.get('problema')
        problemas = Problema.objects.filter(area_id=area_id).order_by('desc_problema')

        return render (request, 'misc/problemas_dropdown_list.html', {'problemas' : problemas})

    elif request.method == 'GET' and 'cat_problema' in request.GET:

        problema_id = request.GET.get('cat_problema')
        cat_problemas = Categoria_Problema.objects.filter(
                problema_id=problema_id).values(
                    'id',
                    'problema__desc_problema',
                    'desc_categoria_problema',
                    'sla',
                    'tipo_manutencao',
                    'origem'
                )
        return render (request, 'misc/cat_problemas_options_list.html', {'cat_problemas' : cat_problemas} )

# def teste_json(request):

#     area_id = request.GET.get('area')
#     problemas = Problema.objects.filter(area_id=area_id).order_by('desc_problema')
#     problemas_json = serializers.serialize('json', problemas)

#     return HttpResponse(problemas_json, content_type='application/json')


# def load_cat_problemas(request):

#     problema_id = request.GET.get('problema')
#     cat_problemas = Categoria_Problema.objects.filter(problema_id=problema_id).order_by('desc_categoria_problema')
#     cat_problemas_json = serializers.serialize('json', cat_problemas)
#     print(cat_problemas_json)
#     return HttpResponse(cat_problemas_json, content_type='application/json')


# def home(request):
#     ''' Lista de Chamados na Tela Inicial '''

#     lista_chamados = Chamado.objects.all().order_by('id')
#     paginator = Paginator(lista_chamados, 4, 0)
#     page = request.GET.get('page')
#     p = paginator.get_page(page)

#     ''' Criar Chamado '''

#     if request.method == 'POST':
#         form = CriaChamado(request.POST)

#         if form.is_valid():

#             return render(request, 'home.html', {
#                 'p': p,
#                 'lista_chamados': lista_chamados,
#                 'form': form

#             })

#     else:
#         form = CriaChamado()

#     return render(request, 'home.html', {
#         'p': p,
#         'lista_chamados': lista_chamados,
#         'form': form,
#     })

# def ajax_load_select(request):

#     areas = Area.objects.all()
#     problemas= Problema.objects.filter(areas=id)

#     json.dumps(problema)
#     json.dumps(area)

#     return render_to_response("ajax.html", {'areas':area,'problemas':problemas})


# def home_cards(request):

#     lista_chamados = Chamado.objects.all().order_by('id')
#     paginator = Paginator(lista_chamados, 4, 0)
#     page = request.GET.get('page')
#     p = paginator.get_page(page)

#     return render(request, 'home_cards.html', {
#         'p': p,
#         'lista_chamados': lista_chamados
#     })


# def login(request):

#     return render(request, 'login.html', {})


# def consultar(request):

#     return render(request, 'consultar.html', {})


# def editar(request):

#     return render(request, 'editar.html', {})


# def encerrar(request):

#     return render(request, 'encerrar.html', {})
