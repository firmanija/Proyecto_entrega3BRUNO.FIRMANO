Proyecto_entrega3
Proyecto Django (Blog) de entrega — patrón MVT.
Incluye modelos: Autor, Categoria, Post; formularios para crear cada modelo; búsqueda por título; plantillas con herencia.

Requisitos
Python 3.10+
pip
Virtualenv (recomendado)
Estructura principal
Proyecto_entrega3/
manage.py
Proyecto_entrega3/ (settings, urls, wsgi)
AppBlog/ (models, views, forms, templates)
templates/ (base.html)
templates2/ (alternativa si se usó)
venv/ (entorno virtual)
db.sqlite3
Instalación (Windows / PowerShell)
Clonar:
git clone 
cd Proyecto_entrega3

Crear y activar venv:
python -m venv venv
.\venv\Scripts\Activate.ps1

Instalar dependencias:
python -m pip install -r requirements.txt
(si no existe: python -m pip install "django>=4.2")

Migraciones:
python manage.py makemigrations
python manage.py migrate

(Opcional) Crear superusuario:
python manage.py createsuperuser

Ejecutar servidor:
python manage.py runserver
Abrir: http://127.0.0.1:8000/

Rutas importantes
/ — lista de posts (index)
/post/crear/ — crear Post
/autor/crear/ — crear Autor
/categoria/crear/ — crear Categoría
/buscar/ — buscar posts por título (GET param q)
/post/<id>/ — detalle del post
/admin/ — panel administrativo
Notas:

Crear Autor y Categoría antes de crear Post (puedes usar Admin o las rutas públicas).
Formularios usan {% csrf_token %} y método POST.
Archivos clave
AppBlog/models.py — Autor, Categoria, Post
AppBlog/forms.py — formularios (AutorForm, CategoriaForm, PostForm, BuscarForm)
AppBlog/views.py — vistas (index, crear_*, buscar, detalle)
AppBlog/urls.py — rutas de la app
Proyecto_entrega3/urls.py — incluye AppBlog.urls
templates/base.html y AppBlog/templates/AppBlog/*.html — plantillas (herencia)
.gitignore recomendado
text

Collapse


 Copy

venv/
__pycache__/
db.sqlite3
*.pyc
.vscode/
requirements.txt
Generar desde el venv:

text

Collapse


 Copy

python -m pip freeze > requirements.txt
(Como mínimo: Django>=4.2)

Subir a GitHub (resumen)
git init (si no está)
git remote add origin
git add .
git commit -m "Proyecto_entrega3: inicial"
git branch -M main
git push -u origin main
Comprobaciones y problemas comunes
TemplateDoesNotExist: revisar TEMPLATES['DIRS'] y rutas de plantillas.
Error CSRF: asegurar {% csrf_token %} y method="post".
Si el servidor no arranca, leer la traza en terminal (indica archivo y línea con el problema).
