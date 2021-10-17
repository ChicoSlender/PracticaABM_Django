from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Empleado

# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'


class CrearEmpleado(CreateView):
    model = Empleado
    fields = ['nombre', 'apellido', 'salario']


class VerEmpleados(ListView):
    model = Empleado


class DetalleEmpleado(DetailView):
    model = Empleado


class BorrarEmpleado(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados')


class EditarEmpleado(UpdateView):
    model = Empleado
    fields = ['salario']