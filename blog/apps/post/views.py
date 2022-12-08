from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def crearPost(request):
    if request.method=='POST':
        post_form=PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('crear_post')
    else:
        post_form=PostForm()
    return render(request,  'post/index.html',{'post_form':post_form})
