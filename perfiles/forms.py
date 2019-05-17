from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.core.files.images import get_image_dimensions


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

       # def clean_imagen(self):
        #    imagen = self.clean_imagen()

        #   try:
        #       w, h = get_image_dimensions(imagen)

                # validar dimensiones de la imagen

        #       max_whidth = max_height = 100
        #       if w > max_whidth or h > max_height:
        #           raise forms.ValidationError(
        #               u'Por favor usa una imagen del siguiente tamaño'
        #               '%s x %s pixeles o mas grande' % (max_whidth, max_height))
        #
        #       # validar el contenido de la imagen
        #
        #       main, sub = imagen.content_type.split('/')
        #       if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
        #           raise forms.ValidationError(u'Please use a JPEG,'
        #                                       'GIF or PNG image.')

        #       # validacion del tamaño de archivo
        #       if len(imagen) > (20 * 1024):
        #           raise forms.ValidationError(u'la imagen no puede superar un ta,año de 25')
        #   except AttributeError:
        #       """Si no agregamos imagen"""
        #       pass
    #       return imagen