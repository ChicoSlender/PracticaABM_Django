from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('empleado/add', views.CrearEmpleado.as_view(), name="agregar-empleado"),
    path('empleado/edit/<int:pk>', views.EditarEmpleado.as_view(), name="editar-empleado"),
    path('empleados', views.VerEmpleados.as_view(), name='empleados'),
    path('empleado/<int:pk>', views.DetalleEmpleado.as_view(), name='detalle-empleado'),
    path('empleado/borrar/<int:pk>', views.BorrarEmpleado.as_view(), name="borrar-empleado"),
]