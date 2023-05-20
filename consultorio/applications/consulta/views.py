from django.shortcuts import render

from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView
)# Create your views here.
from .models import Consulta
from .forms import ConsultaForm
from django.urls import reverse_lazy
from applications.users.models import Patient
from django.shortcuts import get_object_or_404
from applications.users.mixins import AdminPermisoMixin


class HistorialConsultas(AdminPermisoMixin, ListView):
    template_name = 'consulta/historial_consulta.html'
    context_object_name = 'consultas'
    
    
    def get_queryset(self):
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(Patient, id=patient_id)
        return Consulta.objects.historial_consulta_paciente(patient)

    def get_context_data(self, **kwargs):
        context = super(HistorialConsultas,self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        consulta = get_object_or_404(Consulta.objects.filter(patient__id=pk).order_by('-created_at')[:1])
        
        # Calcular el IMC
        peso = consulta.peso
        altura = consulta.patient.altura 
        imc = peso / (altura * altura)
        
        context['imc'] = imc
        context['paciente'] = Patient.objects.filter(id=pk)
        return context



class ConsultaCreateView(AdminPermisoMixin, CreateView):
    model = Consulta
    template_name = "consulta/add_consulta.html"
    form_class = ConsultaForm
    success_url = reverse_lazy('users_app:user-lista-patient')

    def form_valid(self, form):
        
        patient_id = self.kwargs['pk']
        patient = get_object_or_404(Patient, id=patient_id)
        consulta = form.save(commit=False)
        consulta.patient = patient
        consulta.created_by = self.request.user
        consulta.save()
        return super(ConsultaCreateView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ConsultaCreateView,self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context['paciente'] = Patient.objects.filter(id=pk)
        return context

   
   
