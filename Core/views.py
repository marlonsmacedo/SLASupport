from datetime import datetime, timezone

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ChamadoCreateForm, ChamadoDetailForm, ChamadoUpdateForm
from .models import Area, Categoria_Problema, Chamado, Problema


class ChamadoListView(LoginRequiredMixin, ListView):

    model = Chamado
    ordering = '-id'
    context_object_name = 'chamado'
    paginate_by = 4
    login_url = 'acesso/login/'
    redirect_field_name = 'redirect_to'



class ChamadoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Chamado
    form_class = ChamadoCreateForm
    success_url = reverse_lazy('home')
    success_message = "Ocorrência aberta com Sucesso no Sistema."
    login_url = 'acesso/login/'
    redirect_field_name = 'redirect_to'

    def get_initial(self):

        user = self.request.user
        initial = {'criador': user}
        return initial


class ChamadoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Chamado
    form_class = ChamadoUpdateForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home')
    success_message = "Ocorrência Alterada com Sucesso!"
    login_url = 'acesso/login/'
    redirect_field_name = 'redirect_to'


class ChamadoDetailView(LoginRequiredMixin, DetailView):
    model = Chamado
    template_name_suffix = '_detail_form'
    form_class = ChamadoDetailForm
    login_url = 'acesso/login/'
    redirect_field_name = 'redirect_to'

    def get_object(self, queryset=None):
        """
        Return the object the view is displaying.
        Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
        Subclasses can override this to return any object.
        """
        # Use a custom queryset if provided; this is required for subclasses
        # like DateDetailView
        if queryset is None:
            queryset = self.get_queryset()
        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        slug = self.kwargs.get(self.slug_url_kwarg)
        if pk is not None:
            queryset = queryset.filter(pk=pk)
        # Next, try looking up by slug.
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{slug_field: slug})
        # If none of those are defined, it's an error.
        if pk is None and slug is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk or a slug in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                        {'verbose_name': queryset.model._meta.verbose_name})
        return obj

@login_required
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
