from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, AutorForm, CategoriaForm, BuscarForm

def index(request):
    posts = Post.objects.order_by('-creado')[:20]
    return render(request, 'AppBlog/index.html', {'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'AppBlog/detalle_post.html', {'post': post})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'AppBlog/post_form.html', {'form': form})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'AppBlog/autor_form.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'AppBlog/categoria_form.html', {'form': form})

def buscar(request):
    form = BuscarForm(request.GET or None)
    resultados = []
    q = ''
    if form.is_valid():
        q = form.cleaned_data.get('q')
        if q:
            resultados = Post.objects.filter(titulo__icontains=q)
    return render(request, 'AppBlog/buscar.html', {'form': form, 'resultados': resultados, 'q': q})