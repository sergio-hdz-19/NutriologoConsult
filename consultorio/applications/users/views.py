from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .mixins import AdminPermisoMixin, AssistantPermisoMixin

from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView,
    DetailView
)

from django.views.generic.edit import (
    FormView
)

from .forms import (
    UserRegisterForm, 
    LoginForm,
    UserUpdateForm,
    UpdatePasswordForm,
    PatientRegisterForm,
    PatientUpdateForm,
)
#
from .models import User, Patient
from applications.consulta.models import Consulta


class Home(TemplateView):
    template_name = 'home/index.html'


class UserRegisterView(AdminPermisoMixin,FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user-lista')

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['password1'],
            name=form.cleaned_data['name'],
            last_name=form.cleaned_data['last_name'],
            ocupation=form.cleaned_data['ocupation'],
            gender=form.cleaned_data['gender'],
        )
        return super(UserRegisterView, self).form_valid(form)



class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users_app:home')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )



class UserUpdateView(AdminPermisoMixin, UpdateView):
    template_name = "users/update.html"
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users_app:user-lista')


class UserDeleteView(AdminPermisoMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users_app:user-lista')


class UpdatePasswordView(AdminPermisoMixin, LoginRequiredMixin, FormView):
    template_name = 'users/update.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user-login')
    login_url = reverse_lazy('users_app:user-login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1']
        )

        if user:
            new_password = form.cleaned_data['password2']
            usuario.set_password(new_password)
            usuario.save()

        logout(self.request)
        return super(UpdatePasswordView, self).form_valid(form)


class UserListView(AdminPermisoMixin, ListView):
    template_name = "users/lista.html"
    context_object_name = 'usuarios'

    def get_queryset(self):
        return User.objects.usuarios_administradores()
    
class AssistantListView(AdminPermisoMixin, ListView):
    template_name = "users/list_assistant.html"
    context_object_name = 'asistentes'

    def get_queryset(self):
        return User.objects.usuarios_asistentes()
    
class PatientListView(AdminPermisoMixin, ListView):
    template_name = "users/list_patient.html"
    context_object_name = 'pacientes'
    paginate_by = 4
    ordering = 'last_name'
    
    
    def get_queryset(self):
        return Patient.objects.usuarios_pacientes()
    
    
    
    
    


class PatientRegisterView(AdminPermisoMixin, FormView):
    template_name = 'users/register_patient.html'
    form_class = PatientRegisterForm
    success_url = reverse_lazy('users_app:user-lista-patient')

    def form_valid(self, form):
        #
        Patient.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['password1'],
            name=form.cleaned_data['name'],
            last_name=form.cleaned_data['last_name'],
            ocupation=User.PATIENT,
            gender=form.cleaned_data['gender'],
            date_birth=form.cleaned_data['date_birth'],
            peso=form.cleaned_data['peso'],
            altura=form.cleaned_data['altura'],
            actividad_aerobica=form.cleaned_data['actividad_aerobica'],
        )
        return super(PatientRegisterView, self).form_valid(form)




class PatientUpdateView(AdminPermisoMixin, UpdateView):
    template_name = "users/update_patient.html"
    model = Patient
    form_class = PatientUpdateForm
    success_url = reverse_lazy('users_app:user-lista-patient')
    
    
    
class PatientDetailView(AdminPermisoMixin, DetailView):
    model = Patient
    template_name = "users/patient_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView,self).get_context_data(**kwargs)
        return context
    
    
    
    def get_context_data(self, **kwargs):
        context = super(PatientDetailView,self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        # consulta = get_object_or_404(Consulta.objects.filter(patient__id=pk).order_by('-created_at')[:1])
        # context['paciente'] = Patient.objects.filter(id=pk)
        # Verificar si el usuario tiene una consulta asociada
        
        consulta_exists = Consulta.objects.filter(patient__id=pk).exists()
        
        context['paciente'] = Patient.objects.filter(id=pk)
        context['consulta_exists'] = consulta_exists
        return context
    
    
    




class PatientListViewAssistant(AssistantPermisoMixin,ListView):
    template_name = "assistant/list_patient.html"
    context_object_name = 'pacientes'
    # paginate_by = 4
    ordering = 'last_name'
    model = Patient
    
    
    
class PatientDetailViewAssistant(AssistantPermisoMixin,DetailView):
    model = Patient
    template_name = "assistant/patient_detail_assistant.html"

    def get_context_data(self, **kwargs):
        context = super(PatientDetailViewAssistant,self).get_context_data(**kwargs)
        return context



class PatientStatus(ListView):
    template_name = 'patient/status_paciente.html'
    context_object_name = 'consultas'
    
    
    
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        if palabra_clave:
            return Consulta.objects.historial_consulta_by_id(palabra_clave)
        else:
            return Consulta.objects.none()
