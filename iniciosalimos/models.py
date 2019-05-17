# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorias(models.Model):
    idcategoria = models.AutoField(db_column='IdCategoria', primary_key=True)  # Field name made lowercase.
    detalle = models.CharField(db_column='Detalle', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorias'


class Ciudad(models.Model):
    idciudad = models.AutoField(db_column='IdCiudad', primary_key=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=45)  # Field name made lowercase.
    iddepartamento = models.PositiveIntegerField(db_column='IdDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ciudad'


class Comentario(models.Model):
    idcomentario = models.AutoField(db_column='IdComentario', primary_key=True)  # Field name made lowercase.
    idevento = models.PositiveIntegerField(db_column='IdEvento')  # Field name made lowercase.
    idlugar = models.PositiveIntegerField(db_column='IdLugar')  # Field name made lowercase.
    idfuncion = models.PositiveIntegerField(db_column='IdFuncion')  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=7, blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=44, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comentario'


class Departamentos(models.Model):
    iddepartamento = models.CharField(db_column='IdDepartamento', max_length=14, blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='Departamento', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamentos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Edades(models.Model):
    idedad = models.CharField(db_column='IdEdad', max_length=6, blank=True, null=True)  # Field name made lowercase.
    edad = models.CharField(db_column='Edad', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'edades'


class Eventos(models.Model):
    idevento = models.AutoField(db_column='IdEvento', primary_key=True)  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre')  # Field name made lowercase.
    idcategoria = models.IntegerField(db_column='IdCategoria')  # Field name made lowercase.
    detalle = models.TextField(db_column='Detalle')  # Field name made lowercase.
    fechainicio = models.DateField(db_column='FechaInicio')  # Field name made lowercase.
    fechafinal = models.DateField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    idedad = models.IntegerField(db_column='IdEdad', blank=True, null=True)  # Field name made lowercase.
    iddepartamento = models.IntegerField(db_column='IdDepartamento', blank=True, null=True)  # Field name made lowercase.
    contacto = models.TextField(db_column='Contacto', blank=True, null=True)  # Field name made lowercase.
    idciudad = models.PositiveIntegerField(db_column='IdCiudad')  # Field name made lowercase.
    paginaweb = models.IntegerField(db_column='PaginaWeb', blank=True, null=True)  # Field name made lowercase.
    direccion = models.IntegerField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.IntegerField(db_column='Ubicacion', blank=True, null=True)  # Field name made lowercase.
    horacomienzo = models.IntegerField(db_column='HoraComienzo', blank=True, null=True)  # Field name made lowercase.
    nombreimagen = models.TextField(db_column='NombreImagen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventos'


class Favoritos(models.Model):
    idfavoritos = models.AutoField(db_column='Idfavoritos', primary_key=True)  # Field name made lowercase.
    idcategoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='IdCategoria')  # Field name made lowercase.
    idusuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='IdUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'favoritos'


class Funciones(models.Model):
    idfuncion = models.AutoField(db_column='IdFuncion', primary_key=True)  # Field name made lowercase.
    idlugar = models.PositiveIntegerField(db_column='IdLugar')  # Field name made lowercase.
    funcion = models.CharField(db_column='Funcion', max_length=37, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    hora = models.TimeField(db_column='Hora', blank=True, null=True)  # Field name made lowercase.
    idedad = models.PositiveIntegerField(db_column='IdEdad', blank=True, null=True)  # Field name made lowercase.
    fotofuncion = models.CharField(db_column='FotoFuncion', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'funciones'


class Lugares(models.Model):
    idlugar = models.AutoField(db_column='IdLugar', primary_key=True)  # Field name made lowercase.
    idcategoria = models.IntegerField(db_column='IdCategoria')  # Field name made lowercase.
    nombre = models.TextField(db_column='Nombre')  # Field name made lowercase.
    iddepartamento = models.IntegerField(db_column='IdDepartamento')  # Field name made lowercase.
    idciudad = models.PositiveIntegerField(db_column='IdCiudad')  # Field name made lowercase.
    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.
    horario = models.TextField(db_column='Horario', blank=True, null=True)  # Field name made lowercase.
    telefono = models.TextField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    tarjetas = models.TextField(db_column='Tarjetas', blank=True, null=True)  # Field name made lowercase.
    pagina = models.TextField(db_column='Pagina', blank=True, null=True)  # Field name made lowercase.
    tipocomida = models.TextField(db_column='TipoComida', blank=True, null=True)  # Field name made lowercase.
    gastopromedio = models.TextField(db_column='GastoPromedio', blank=True, null=True)  # Field name made lowercase.
    servicios = models.TextField(db_column='Servicios', blank=True, null=True)  # Field name made lowercase.
    ubicaciongoogle = models.TextField(db_column='UbicacionGoogle', blank=True, null=True)  # Field name made lowercase.
    nombreimagen = models.TextField(db_column='NombreImagen', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lugares'


class PerfilesPerfil(models.Model):
    bio = models.CharField(max_length=255)
    web = models.CharField(max_length=200)
    imagen = models.CharField(max_length=100)
    usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'perfiles_perfil'
