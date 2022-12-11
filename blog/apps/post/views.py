from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
#from Modulos.Academica.plantillas import *
from django.contrib import messages

# Create your views here.
def plantillaHija1(request):
    return render(request, "plantillaHija1.html", {})

def plantillaHija2(request):
    return render(request, "plantillaHija2.html", {})
def blog(request):
    return render(request, "blog.html", {})
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
