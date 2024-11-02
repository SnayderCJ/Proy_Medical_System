from django.urls import path
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
from aplication.core.views.tipoSangre import TipoSangreListView, TipoSangreCreateView, TipoSangreUpdateView, TipoSangreDeleteView, TipoSangreDetailView
from aplication.core.views.especialidad import EspecialidadListView, EspecialidadCreateView, EspecialidadUpdateView, EspecialidadDeleteView, EspecialidadDetailView
from aplication.core.views.doctor import DoctorListView, DoctorCreateView # Seguir con las rutas de doctor
from aplication.core.views.cargo import CargoListView, CargoCreateView, CargoUpdateView, CargoDeleteView, CargoDetailView

app_name='core' # define un espacio de nombre para la aplicacion

urlpatterns = [
  # ruta principal
  path('', HomeTemplateView.as_view(),name='home'),
  # rutas doctores VBF
  # path('doctor_list/', views.doctor_List,name="doctor_list"),
  # path('doctor_create/', views.doctor_create,name="doctor_create"),
  # path('doctor_update/<int:id>/', views.doctor_update,name='doctor_update'),
  # path('doctor_delete/<int:id>/', views.doctor_delete,name='doctor_delete'),
  # rutas doctores VBC
  path('patient_list/',PatientListView.as_view() ,name="patient_list"),
  path('patient_create/', PatientCreateView.as_view(),name="patient_create"),
  path('patient_update/<int:pk>/', PatientUpdateView.as_view(),name='patient_update'),
  path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
  path('patient_detail/<int:pk>/', PatientDetailView.as_view(),name='patient_detail'),
  
  # Tipo de Sangre
  path('tipoSangre_list/', TipoSangreListView.as_view(), name="tipoSangre_list"),
  path('tipoSangre_create/', TipoSangreCreateView.as_view(), name="tipoSangre_create"),
  path('tipoSangre_update/<int:pk>/', TipoSangreUpdateView.as_view(), name="tipoSangre_update"),
  path('tipoSangre_delete/<int:pk>/', TipoSangreDeleteView.as_view(), name="tipoSangre_delete"),
  path('tipoSangre_detail/<int:pk>/', TipoSangreDetailView.as_view(), name="tipoSangre_detail"),
  
  # Especialidad
  path('especialidad_list/', EspecialidadListView.as_view(), name="especialidad_list"),
  path('especialidad_create/', EspecialidadCreateView.as_view(), name="especialidad_create"),
  path('especialidad_update/<int:pk>/', EspecialidadUpdateView.as_view(), name="especialidad_update"),
  path('especialidad_delete/<int:pk>/', EspecialidadDeleteView.as_view(), name="especialidad_delete"),
  path('especialidad_detail/<int:pk>/', EspecialidadDetailView.as_view(), name="especialidad_detail"),
  
  # Doctor
  path('doctor_list/', DoctorListView.as_view(), name="doctor_list"),
  path('doctor_create/', DoctorCreateView.as_view(), name="doctor_create"),
  # Seguir con las rutas de doctor
  
  # Cargo 
  path('cargo_list/', CargoListView.as_view(), name="cargo_list"),
  path('cargo_create/', CargoCreateView.as_view(), name="cargo_create"),
  path('cargo_update/<int:pk>/', CargoUpdateView.as_view(), name="cargo_update"),
  path('cargo_delete/<int:pk>/', CargoDeleteView.as_view(), name="cargo_delete"),
  path('cargo_detail/<int:pk>/', CargoDetailView.as_view(), name="cargo_detail"),
  
]