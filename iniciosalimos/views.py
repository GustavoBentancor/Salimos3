import pymysql
import pymysql._socketio
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

from iniciosalimos import models


def inicio(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    Lista_comentarios = cursor.execute("select * from salimos.comentario where IdEvento=0 and IdFuncion=0 and IdLugar=0 order by idComentario desc limit 10")
    return render(request, "inicio/index.html", {'comentarios': Lista_comentarios})


def cine_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute(
        "Select L.*, salimos.departamentos.Departamento from salimos.lugares L, salimos.departamentos D where L.IdCategoria in (3) AND D.IdDepartamento=L.IdDepartamento")
    Cine = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Cine/Cine.html', {'Cine': Cine})


def detalle_cine_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    Detalle_Cine = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Cine/Detalle_Cine.html', {'item': Detalle_Cine[0]})


def festi_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute('select E.*, departamento departamento from eventos E, departamentos D where E.IdCategoria in (4,11) AND D.IdDepartamento=E.IdDepartamento')
    Festivales = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Festivales/Festivales.html', {'Festivales': Festivales})


def detalle_festi_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detalle_Festivales = request.GET.get('id_Festivales', 0)
    Detalle_Festivales = cursor.execute("Select * from Eventos where IdEvento=" + id_Detalle_Festivales)
    Detalle_Festivales = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Festivales/Detalle_Festivales.html', {'item': Detalle_Festivales[0]})


def crio_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute(
        "Select E.*, D.Departamento from Eventos E, Departamentos D where E.IdCategoria in (4,1) AND D.IdDepartamento=E.IdDepartamento")
    Criollas = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Criollas/Criollas.html', {'Criollas': Criollas})


def detalle_crio_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detalle_Criollas = request.GET.get('id_Criollas', 0)
    Detalle_Criollas = cursor.execute("Select * from Eventos where IdEvento=" + id_Detalle_Criollas)
    Detalle_Criollas = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Criollas/Detalle_Criollas.html', {'item': Detalle_Criollas[0]})


def gastro_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute(
        "Select L.*, D.Departamento from Lugares L, Departamentos D where L.IdCategoria in (2,8) AND D.IdDepartamento=L.IdDepartamento")
    Gastronomia = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Gastronomia/Gastronomia.html', {'Gastronomia': Gastronomia})


def detalle_gastro_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detalle_Gastronomia = request.GET.get('id_Gastronomia', 0)
    Detalle_Gastronomia = cursor.execute("Select * from Lugares where IdLugar=" + id_Detalle_Gastronomia)
    Detalle_Gastronomia = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Gastronomia/Detalle_Gastronomia.html', {'item': Detalle_Gastronomia[0]})


def teatro_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute(
        "Select L.*, D.Departamento from Lugares L, Departamentos D where L.IdCategoria in (5) AND D.IdDepartamento=L.IdDepartamento")
    Teatros = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Teatros/Teatros.html', {'Teatros': Teatros})


def detalle_teatros_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detalle_Teatros = request.GET.get('id_Teatros', 0)
    Detalle_Teatros = cursor.execute(
        "Select L.*, F.Funcion, F.Fecha, F.Hora from Lugares L,Funiciones F where L.IdLugar=" + id_Detalle_Teatros + " AND F.IdLugar=" + id_Detalle_Teatros)
    Detalle_Teatros = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Teatros/Detalle_Teatros.html', {'item': Detalle_Teatros[0]})


def toques_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute(
        "Select E.*, D.Departamento from Eventos E, Departamentos D where E.IdCategoria in (6) AND D.IdDepartamento=E.IdDepartamento")
    Toques = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Toques/Toques.html', {'Toques': Toques})


def detalle_toques_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detalle_Toques = request.GET.get('id_Toques', 0)
    Detalle_Toques = cursor.execute("Select * from Eventos where IdEvento=" + id_Detalle_Toques)
    Detalle_Toques = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Toques/Detalle_Toques.html', {'item': Detalle_Toques[0]})


def boli_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute("Select L.*, D.Departamento from Lugares L, Departamentos D where L.IdCategoria in (8,9) AND D.IdDepartamento=L.IdDepartamento")
    Boliches = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Boliches/Boliches.html', {'Boliches': Boliches})


def detalle_boli_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detalle_Boliches = request.GET.get('id_Boliches', 0)
    Detalle_Boliches = cursor.execute("Select * from Lugares where IdLugar=" + id_Detalle_Boliches)
    Detalle_Boliches = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Boliches/Detalle_Boliches.html', {'item': Detalle_Boliches[0]})


def artdep_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute(
        "Select E.*, D.Departamento from salimos.eventos E, Departamentos D where E.IdCategoria in (10) AND D.IdDepartamento=E.IdDepartamento")
    Artdep = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Artdep/Artdep.html', {'Artdep': Artdep})


def detalle_artdep_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detalle_Artdep = request.GET.get('id_Artdep', 0)
    Detalle_Artdep = cursor.execute("Select * from salimos.eventos where IdEvento=" + id_Detalle_Artdep)
    Detalle_Artdep = cursor.fetchall()
    db.commit()
    return render_to_response('Categorias/Artdep/Detalle_Artdep.html', {'item': Detalle_Artdep[0]})


def enfamilia_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdEdad in (1) ")
    Lugar = cursor.fetchall()
    db.commit()
    return render_to_response('Mievento/Enfamilia/enfamilia.html', {'Lugar': Lugar})


def conamigos_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdCategoria in (6,7,9,10,11) and IdEdad in (4,5)")
    Evento = cursor.fetchall()
    db.commit()
    return render_to_response('Mievento/Conamigos/conamigos.html', {'Evento': Evento})


def Detalleconamigos_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detalle_Conamigos = request.GET.get('id_Conamigos', 0)
    Detalle_Conamigos = cursor.execute("Select * from Eventos where IdEvento=" + id_Detalle_Conamigos)
    db.commit()
    return render_to_response('Mievento/Conamigos/Detalle_conamigos.html', {'item': Detalle_Conamigos.fetchone()})


def ninos_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute("Select * from Eventos where IdEdad in (2)")
    Evento = cursor.fetchall()
    db.commit()
    return render_to_response('Mievento/Paraninos/ninos.html', {'Evento': Evento})


def Detalleninos_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detalle_Ninos = request.GET.get('id_DetalleNinos', 0)
    DetalleNinos = cursor.execute("Select * from Eventos where IdEvento=" + id_Detalle_Ninos)
    db.commit()
    return render_to_response('Mievento/Paraninos/paraninos.html', {'item': DetalleNinos.fetchone()})


def paseos_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares where IdLugar in (10)")
    Lugar = cursor.fetchall()
    db.commit()
    return render_to_response('Mievento/Paseos/paseos.html', {'Lugar': Lugar})


def Detallepaseos_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detallepaseo = request.GET.get('id_Detallepaseo', 0)
    dtallepaseo = cursor.execute("Select * from Lugares where IdLugar=" + id_Detallepaseo)
    db.commit()
    return render_to_response('Mievento/Paseos/Detalle_paseos.html', {'item': dtallepaseo.fetchone()})


def turismo_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    cursor.execute("Select * from Lugares where IdCategoria in (12)")
    Lugart = cursor.fetchall()
    db.commit()
    return render_to_response('Mievento/LugaresTuri/turismo.html', {'Lugart': Lugart})


def Detalleturismo_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_Detalleturi = request.GET.get('id_detalleturi', 0)
    dtalleturi = cursor.execute("Select * from Lugares where IdLugar=" + id_Detalleturi)
    db.commit()
    return render_to_response('Mievento/LugaresTuri/Detalle_Lugaresturi.html', {'item': dtalleturi.fetchone()})


def airlib_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    Evento = cursor.execute("select Eventos.Nombre ,Eventos.Detalle, Eventos.Ciudad from Eventos")
    db.commit()
    return render_to_response('Mievento/LugaresTuri/turismo.html', {'Evento': Evento})


def montevideo_inicio_list(request):
    return render_to_response('Departamentos/Montevideo_inicio.html')


def montevideo_eventos_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    # cursor.execute("Select * from Eventos")
    Montevideo = cursor.execute("select * from eventos where eventos.IdDepartamento=10")
    db.commit()
    return render_to_response('Departamentos/Montevideo_eventos.html', {'Montevideo': Montevideo})


def montevideo_lugares_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    # cursor.execute("Select * from Eventos")
    Montevideo = cursor.execute("select * from lugares where iddepartamento=10")
    db.commit()
    return render_to_response('Departamentos/Montevideo_lugares.html', {'Montevideo': Montevideo})


def rocha_inicio_list(request):
    return render_to_response('Departamentos/Rocha_inicio.html')


def rocha_eventos_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    Rocha = cursor.execute("select * from eventos where eventos.IdDepartamento=14")
    db.commit()
    return render_to_response('Departamentos/Rocha_eventos.html', {'Rocha': Rocha})


def rocha_lugares_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    Rocha = cursor.execute("select * from lugares where iddepartamento=14")
    db.commit()
    return render_to_response('Departamentos/Rocha_lugares.html', {'Rocha': Rocha})


def detalle_eventos_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_detalle_evento = request.GET.get('id_evento', 0)
    db.commit()
    # Detalle_eventos = cursor.execute("select * from eventos where idevento=" + id_detalle_evento)
    # cursor = db.cursor()
    # Lista_coment = cursor.execute("select * from comentario where idevento=" + id_detalle_evento+" order by idcomentario desc" )

    # return render_to_response('Departamentos/Detalle_eventos.html', {'item': Detalle_eventos.fetchone(),'comentarios':Lista_coment})
    return retorno_evento_comentario(id_detalle_evento, 'E')


def detalle_lugares_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_detalle_lugar = request.GET.get('id_lugar', 0)
    Detalle_lugares = cursor.execute("select * from lugares where idlugar=" + id_detalle_lugar)
    db.commit()
    return retorno_evento_comentario(id_detalle_lugar, 'L')
    # return render_to_response('Departamentos/Detalle_lugares.html', {'item': Detalle_lugares.fetchone()})


def Detalleenfamilia_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    id_detalle_enfamilia = request.GET.get('id_enfamilia', 0)
    detalle_enfamilia = cursor.execute("select * from eventos where  eventos.IdEvento =" + id_detalle_enfamilia)
    db.commit()
    return render_to_response('Mievento/Enfamilia/Detalle_enfamilia.html', {'item': detalle_enfamilia})


def Comentar_id(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    tipo = request.GET.get('tipo', 0)
    id = request.GET.get('id', 0)
    if tipo == 'E' or tipo == 'F' or tipo == 'A' or tipo == 'Cr' or tipo == 'To':
        texto_evento = request.GET.get('comentario', 0)
        Agregar_evento = cursor.execute(
            "Insert into Comentario (idevento,Comentario) values (" + id + ",'" + texto_evento + "')")
        db.commit()
    elif tipo == 'L' or tipo == 'G' or tipo == 'B' or tipo == 'Ci' or tipo == 'Te':
        texto_lugar = request.GET.get('comentario', 0)
        Agregar_lugar = cursor.execute(
            "Insert into Comentario (idlugar,Comentario) values (" + id + ",'" + texto_lugar + "')")
        db.commit()

    # Detalle_eventos = cursor.execute("select * from eventos where idevento=" + id_evento)
    # cursor = db.cursor()
    # Lista_comentarios = cursor.execute("select * from comentario where idevento=" + id_evento+" order by idComentario desc ")
    # return render_to_response('Departamentos/Detalle_eventos.html', {'item': Detalle_eventos.fetchone(),'comentarios': Lista_comentarios})
    return retorno_evento_comentario(id, tipo)


def retorno_evento_comentario(id, tipo):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    if tipo == 'E':
        Detalle_eventos = cursor.execute("select * from eventos where idevento=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from comentario where idevento=" + id + " order by idComentario desc ")
        return render_to_response('Departamentos/Detalle_eventos.html',
                                  {'item': Detalle_eventos.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'L':
        Detalle_lugar = cursor.execute("select * from lugares where idlugar=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.comentario where idlugar=" + id + " order by idComentario desc ")
        return render_to_response('Departamentos/Detalle_lugares.html',
                                  {'item': Detalle_lugar.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'F':
        Detalle_Festivales = cursor.execute("select * from eventos where idevento=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.comentario where idevento=" + id + " order by idComentario desc ")
        return render_to_response('Categorias/Festivales/Detalle_Festivales.html',
                                  {'item': Detalle_Festivales.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'G':
        Detalle_Gastronomia = cursor.execute("select * from lugares where idlugar=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.comentario where idlugar=" + id + " order by idComentario desc ")
        return render_to_response('Categorias/Gastronomia/Detalle_Gastronomia.html',
                                  {'item': Detalle_Gastronomia.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'A':
        Detalle_Artdep = cursor.execute("select * from eventos where idevento=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.comentario where idevento=" + id + " order by idComentario desc ")
        return render_to_response('Categorias/Artdep/Detalle_Artdep.html',
                                  {'item': Detalle_Artdep.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'Cr':
        Detalle_Criollas = cursor.execute("select * from eventos where idevento=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.comentario where idevento=" + id + " order by idComentario desc ")
        return render_to_response('Categorias/Criollas/Detalle_Criollas.html',
                                  {'item': Detalle_Criollas.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'To':
        Detalle_Toques = cursor.execute("select * from eventos where idevento=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.comentario where idevento=" + id + " order by idComentario desc ")
        return render_to_response('Categorias/Toques/Detalle_Toques.html',
                                  {'item': Detalle_Toques.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'B':
        Detalle_Boliches = cursor.execute("select * from lugares where idlugar=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.comentario where idlugar=" + id + " order by idComentario desc ")
        return render_to_response('Categorias/Boliches/Detalle_Boliches.html',
                                  {'item': Detalle_Boliches.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'Ci':
        Detalle_Cine = cursor.execute("select * from lugares where idlugar=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.comentario where idlugar=" + id + " order by idComentario desc ")
        return render_to_response('Categorias/Cine/Detalle_Cine.html',
                                  {'item': Detalle_Cine.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'Te':
        Detalle_Teatros = cursor.execute("select * from lugares where idlugar=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.comentario where idlugar=" + id + " order by idComentario desc ")
        return render_to_response('Categorias/Teatros/Detalle_Teatros.html',
                                  {'item': Detalle_Teatros.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'cn':
        Detalleconamigos_list = cursor.execute("select * from Eventos where IdEvento=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.Comentario where IdEvento=" + id + " order by idComentario desc ")
        return render_to_response('Mievento/Conamigos/Detalle_conamigos.html',
                                  {'item': Detalleconamigos_list.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'fm':
        Detalleenfamilia_list = cursor.execute("select * from Eventos where IdEvento=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.Comentario where IdEvento=" + id + " order by idComentario desc ")
        return render_to_response('Mievento/Enfamilia/detalle_enfamilia.html',
                                  {'item': Detalleenfamilia_list.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'nn':
        Detalleninos_list = cursor.execute("select * from Eventos where IdEvento=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.Comentario where IdEvento=" + id + " order by idComentario desc ")
        return render_to_response('Mievento/Paraninos/paraninos.html',
                                  {'item': Detalleninos_list.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'cn':
        Detallepaseos_list = cursor.execute("select * from Eventos where IdEvento=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.Comentario where IdEvento=" + id + " order by idComentario desc ")
        return render_to_response('Mievento/Paseos/Detalle_paseos.html',
                                  {'item': Detallepaseos_list.fetchone(), 'comentarios': Lista_comentarios})
    elif tipo == 'tr':
        Detalleturismo_list = cursor.execute("select * from salimos.Eventos where IdEvento=" + id)
        cursor = db.cursor()
        Lista_comentarios = cursor.execute(
            "select * from salimos.Comentario where IdEvento=" + id + " order by idComentario desc ")
        return render_to_response('Mievento/LugaresTuri/Detalle_Lugaresturi.html',
                                  {'item': Detalleturismo_list.fetchone(), 'comentarios': Lista_comentarios})


# def retorno_evento_comentario(id_evento):
#   db = sqlite3.connect(database='salimos.db')
#  cursor = db.cursor()
# Detalle_eventos = cursor.execute("select * from eventos where idevento=" + id_evento)
# cursor = db.cursor()
# Lista_comentarios = cursor.execute("select * from comentario where idevento=" + id_evento+" order by idComentario desc ")
# return render_to_response('Departamentos/Detalle_eventos.html', {'item': Detalle_eventos.fetchone(),'comentarios': Lista_comentarios})

def Departamento_opciones(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    depto_id = request.GET.get('id_depto')
    depto = cursor.execute("select * from salimos.departamentos where IdDepartamento=" + depto_id)
    db.commit()
    return render_to_response('Departamentos/Departamento_inicio.html', {'depto': depto})


def Departamento_eventos_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    deptoid = request.GET.get('id_depto')
    depto = cursor.execute("select * from salimos.eventos where IdDepartamento= " + deptoid)
    db.commit()
    return render_to_response('Departamentos/Rocha_eventos.html', {'depto': depto})


def Departamento_lugares_list(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    deptoid = request.GET.get('id_depto')
    Rocha = cursor.execute('select * from salimos.lugares where IdDepartamento =' + deptoid)
    db.commit()
    return render_to_response('Departamentos/Rocha_lugares.html', {'Rochas': Rocha})


def Comentar_todo(request):
    db = pymysql.Connect(host='179.27.81.114', port=6612, user='salimos', password='salimos2019.', database='salimos')
    cursor = db.cursor()
    texto_comentario = request.GET.get('Comentario', 0)
    Agregar_comentario = cursor.execute("Insert into salimos.Comentario (Comentario) values ('" + texto_comentario + "')")
    db.commit()
    return inicio(request)


class BuscarView(TemplateView, Exception):
    def post(self, request, *args, **kwargs):
        obj_nombre = request.POST['buscalo']
        obj = models.Eventos.objects.filter(nombre__contains=obj_nombre)
        lugar = models.Lugares.objects.filter(nombre__contains=obj_nombre)
        ide = request.GET.get('idevento')
        idl = request.GET.get('idlugar')
        for abc in obj, ide, idl, lugar:
            abc.nombre = obj_nombre
            context = {
                "id": ide,
                "obj": obj,
                "idl": idl,
                "lugar": lugar,
                "obj_nombres": obj_nombre,

            }
            # for abce in lugar, idl:
            #   abce.nombre = obj_nombre
            #  context1 = {
            #     "id": idl,
            #    "lugar": lugar,
            #   "obj_nombres": obj_nombre,
            #
            ##               }
            a = render(request, 'eventos/buscar.html', context)
            return a

        # if obj_nombre is not obj:
        #    return render(request, 'mievento.html')

