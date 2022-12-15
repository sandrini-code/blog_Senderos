from django.shortcuts import render, redirect
from .models import Post, Categoria
from .forms import PostForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .forms import UserRegisterForm
#from Modulos.Academica.plantillas import *
from django.contrib import messages
from django.db.models import Q
from datetime import datetime


# Create your views here.
def plantillaHija1(request):
    return render(request, "plantillaHija1.html", {})

def plantillaHija2(request):
    return render(request, "plantillaHija2.html", {})
def blog(request):
    queryset = request.GET.get("buscar")
    cate = request.GET.get("categoria")
    fecha= request.GET.get("fecha")
    meses={"Enero":"01", "Febrero":"02", "Marzo":"03", "Abril":"04", "Mayo":"05", "Junio":"06", "Julio":"07", "Agosto":"08", "Septiembre":"09", "Octubre":"10", "Noviembre":"11", "Diciembre":"12"}
    for mes in meses:
        if mes == fecha:
            mes_Post=meses[mes]
    posts = Post.objects.filter(publicado=True)
    categ = Categoria.objects.all()
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(resumen__icontains=queryset) |
            Q(texto__icontains=queryset)
        ).distinct()
    elif cate and cate!= "Categorias":
        posts = Post.objects.filter(categoria__nombre=cate).distinct()
    elif fecha and fecha!= "Meses":
        posts = Post.objects.filter(
            Q(fecha_creacion__icontains=mes_Post),
        ).distinct()

    context = {
        'posts': posts,
        'categorias': categ
    }
    return render(request, "blog.html", context)
def quienesSomos(request):
    return render(request, "quienesSomos.html", {})
def formularioContacto(request):
    return render(request,"formularioContacto.html")
def contactar(request):
    if request.method == "POST":
        asunto=request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + "/Email " + request.POST["txtEmail"]
        email_desde= settings.EMAIL_HOST_USER
        email_para=["gastonrg9@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")
@login_required
@permission_required("staff")
def crearPost(request):
    if request.method=='POST':
        post_form=PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('crear_post')
    else:
        post_form=PostForm()
    return render(request,  'post/index.html',{'post_form':post_form})


def register (request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f"Usuario {username} creado")
            return redirect(blog)
    else:
        form= UserRegisterForm()

    context={'form' : form}

    return render(request, 'register.html', context)

def publicarPost(request):
    posts= Post.objects.all()
    return render(request, "publicarPost.html", {'posts': posts})
