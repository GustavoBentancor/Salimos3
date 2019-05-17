import pymysql
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render_to_response, render
from django.views.generic import CreateView
from .forms import SignUpForm
from .models import Perfil


class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return render_to_response('perfiles/usuariologueado.html')


# class BienvenidaView(TemplateView):
# render_to_response('perfiles/iniciar_sesion.html')


class SignInView(LoginView):
    template_name = 'perfiles/iniciar_sesion.html'
    redirect_authenticated_user = 'base'


class SignOutView(LogoutView):
    template_name = 'inicio/index.html'
    pass


def base(request):
    return render(request, 'perfiles/usuariologueado.html')


def datos_usuario(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    N_usuario = request.GET.get('username')
    user_data = cursor.execute('select username from salimos.auth_user where id= ' + N_usuario)
    db.commit()


# return render_to_response('perfiles/usuariologueado.html', {'nombre': N_usuario})

ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.12',
    }
}


def favoritos_list():
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    favorito_usuario= cursor.execute("insert into favoritos where  ")