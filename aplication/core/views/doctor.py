from django.urls import reverse_lazy
from aplication.core.forms.doctor import DoctorForm
from aplication.core.models import Doctor
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class DoctorListView(ListView):
    template_name = "doctor/list.html"
    model = Doctor
    context_object_name = 'doctores'
    query = None
    paginate_by = 2
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q') # ver
        if q1 is not None: 
            self.query.add(Q(nombres__icontains=q1), Q.OR) 
            self.query.add(Q(apellidos__icontains=q1), Q.OR) 
            self.query.add(Q(activo__icontains=q1), Q.OR) 
        return self.model.objects.filter(self.query).order_by('apellidos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Doctores"
        return context
    
class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'doctor/form.html'
    form_class = DoctorForm
    success_url = reverse_lazy('core:doctor_list')
    # permission_required = 'add_doctor' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Crear Doctor'
        context['grabar'] = 'Grabar Doctor'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        doctor = self.object
        save_audit(self.request, doctor, action='A')
        messages.success(self.request, f"Éxito al crear al doctor {doctor.nombre_completo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
# class PatientUpdateView(UpdateView):
#     model = Paciente
#     template_name = 'patient/form.html'
#     form_class = PatientForm
#     success_url = reverse_lazy('core:patient_list')
#     # permission_required = 'change_patient'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['grabar'] = 'Actualizar Proveedor'
#         context['back_url'] = self.success_url
#         return context
    
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         patient = self.object
#         save_audit(self.request, patient, action='M')
#         messages.success(self.request, f"Éxito al Modificar el paciente {patient.nombre_completo}.")
#         print("mande mensaje")
#         return response
    
#     def form_invalid(self, form):
#         messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
#         print(form.errors)
#         return self.render_to_response(self.get_context_data(form=form))
    
# class PatientDeleteView(DeleteView):
#     model = Paciente
#     # template_name = 'core/patient/form.html'
#     success_url = reverse_lazy('core:patient_list')
#     # permission_required = 'delete_supplier'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['grabar'] = 'Eliminar Proveedorl'
#         context['description'] = f"¿Desea Eliminar al paciente: {self.object.name}?"
#         context['back_url'] = self.success_url
#         return context
    
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         success_message = f"Éxito al eliminar lógicamente al paciente {self.object.name}."
#         messages.success(self.request, success_message)
#         # Cambiar el estado de eliminado lógico
#         # self.object.deleted = True
#         # self.object.save()
#         return super().delete(request, *args, **kwargs)
    
# class PatientDetailView(DetailView):
#     model = Paciente
    
#     def get(self, request, *args, **kwargs):
#         pacient = self.get_object()
#         data = {
#             'id': pacient.id,
#             'nombres': pacient.nombres,
#             'apellidos': pacient.apellidos,
#             'foto': pacient.get_image(),
#             'fecha_nac': pacient.fecha_nacimiento,
#             'edad': pacient.calcular_edad(pacient.fecha_nacimiento),
#             'dni': pacient.cedula,
#             'telefono': pacient.telefono,
#             'direccion': pacient.direccion,
#             # Añade más campos según tu modelo
#         }
#         return JsonResponse(data)