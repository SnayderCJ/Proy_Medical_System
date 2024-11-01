from django.urls import reverse_lazy
# from aplication.core.forms.tipoSangre import
from aplication.core.models import Especialidad
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class EspecialidadListView(ListView):
    template_name = "especialidad/list.html"
    model = Especialidad
    context_object_name = 'Especialidades'
    query = None
    paginate_by = 2
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q') # ver
        
        if q1 is not None:
            self.query.add(Q(tipo__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('tipo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Especialidades"
        return context
    
    # class EspecialidadCreateView(CreateView):
    #     model = Especialidad
    #     template_name = 'especialidad/form.html'
    #     form_class = EspecialidadForm
    #     success_url = reverse_lazy('core:especialidad_list')

    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data()
    #         context['title1'] = 'Crear Especialidad'
    #         context['grabar'] = 'Grabar Especialidad'
    #         context['back_url'] = self.success_url
    #         return context

    #     def form_valid(self, form):
    #         response = super().form_valid(form)
    #         especialidad = self.object
    #         save_audit(self.request, especialidad, action='A')
    #         messages.success(self.request, f"Éxito al crear la especialidad {especialidad.tipo}.")
    #         return response

    #     def form_invalid(self, form):
    #         messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
    #         print(form.errors)
    #         return self.render_to_response(self.get_context_data(form=form))


    # class EspecialidadUpdateView(UpdateView):
    #     model = Especialidad
    #     template_name = 'especialidad/form.html'
    #     form_class = EspecialidadForm
    #     success_url = reverse_lazy('core:especialidad_list')

    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data()
    #         context['title1'] = 'Actualizar Especialidad'
    #         context['grabar'] = 'Actualizar Especialidad'
    #         context['back_url'] = self.success_url
    #         return context

    #     def form_valid(self, form):
    #         response = super().form_valid(form)
    #         especialidad = self.object
    #         save_audit(self.request, especialidad, action='M')
    #         messages.success(self.request, f"Éxito al modificar la especialidad {especialidad.tipo}.")
    #         return response

    #     def form_invalid(self, form):
    #         messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
    #         print(form.errors)
    #         return self.render_to_response(self.get_context_data(form=form))


    # class EspecialidadDeleteView(DeleteView):
    #     model = Especialidad
    #     success_url = reverse_lazy('core:especialidad_list')

    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data()
    #         context['grabar'] = 'Eliminar Especialidad'
    #         context['description'] = f"¿Desea eliminar la especialidad: {self.object.tipo}?"
    #         context['back_url'] = self.success_url
    #         return context

    #     def delete(self, request, *args, **kwargs):
    #         self.object = self.get_object()
    #         success_message = f"Éxito al eliminar la especialidad {self.object.tipo}."
    #         messages.success(self.request, success_message)
    #         return super().delete(request, *args, **kwargs)


    # class EspecialidadDetailView(DetailView):
    #     model = Especialidad

    #     def get(self, request, *args, **kwargs):
    #         especialidad = self.get_object()
    #         data = {
    #             'id': especialidad.id,
    #             'tipo': especialidad.tipo,
    #             'descripcion': especialidad.descripcion,
    #             # Añade más campos según tu modelo
    #         }
    #         return JsonResponse(data)
