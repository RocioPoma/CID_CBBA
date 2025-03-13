from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from pymysql import NULL
from .models  import  Book, Area,Tesis,Campo,Universidad, Publicity, Magazine,Favorite, Article
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.http import FileResponse, Http404
from PyPDF2 import PdfReader
import io
import unicodedata


def remove_accents(input_str):
    if input_str is None:
        return ''
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)]).lower()

@login_required
def index(request, letter=None):
    if letter is not None:
        normalized_letter = remove_accents(letter.lower())
        books = Book.objects.all()
        books = [book for book in books if remove_accents(book.title).startswith(normalized_letter)]
    else:
        search_term = request.GET.get('search', '').lower()
        try:
            search_id = int(search_term)
        except ValueError:
            search_id = None

        books = Book.objects.all()
        normalized_search_term = remove_accents(search_term)
        books = [book for book in books if (
            normalized_search_term in remove_accents(book.title) or
            normalized_search_term in remove_accents(book.author) or
            normalized_search_term in remove_accents(book.kword) or
            (search_id is not None and book.id == search_id)
        )]

    # Paginación
    paginator = Paginator(books, 5)  # Muestra 5 libros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'books': page_obj,  # Usar 'page_obj' en lugar de 'books'
        'page_obj': page_obj
    }
    return render(request, 'book/bookIndex.html', context)


def view(request, id ):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'book/detailBook.html', context)


def filter_by_area(request):
    select_term = request.GET.get('select', '')

    if select_term:
        books = Book.objects.filter(
            Q(area__areaname__icontains=select_term) |
            Q(area2__areaname__icontains=select_term)
        )
    else:
        books = Book.objects.all()
    
    # Paginación
    paginator = Paginator(books, 5)  # Muestra 10 libros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    areas = Area.objects.distinct()

    context = {
        'books': books,
        'page_obj': page_obj,
        'areas': areas,
        'selected_area': select_term  # Para mantener el área seleccionada en el formulario
    }
    return render(request, 'book/bookIndex.html', context)



def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/partials/modal.html', {'book': book})


@login_required
def tesisIndex(request, letter2 = NULL):
     if letter2 != NULL:
        tesis = Tesis.objects.filter(title__istartswith=letter2)
     else:
        search_term = request.GET.get('search', '')
        try:
            search_id = int(search_term)
        except ValueError:
            search_id = None
        tesis = Tesis.objects.filter(
            Q(title__icontains=search_term) | Q(author__icontains=search_term)|  Q(kword__icontains=search_term)| Q(id=search_id))

     #Paginación
     paginator = Paginator(tesis, 5) #Muestra 10 libros por página
     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)
     context = {
        'tesis': tesis,
        'page_obj': page_obj
        }
     return render(request, 'thesis/thesisIndex.html', context)

def viewTesis(request, id ):
    tesis = Tesis.objects.get(id=id)
    context = {
        'tesis': tesis
    }
    return render(request, 'thesis/detailThesis.html', context)


def filter_by_campo(request):
    select_term = request.GET.get('select', '')

    if select_term:
        tesis = Tesis.objects.filter(campo__campoName__icontains=select_term)
    else:
        tesis = Tesis.objects.all()

    # Paginación
    paginator = Paginator(tesis, 5)  # Muestra 10 libros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    campos = Campo.objects.distinct()

    context = {
        'tesis': tesis,
        'campos': campos,
        'page_obj': page_obj,
        'selected_area': select_term
    }
    return render(request, 'thesis/thesisIndex.html', context)


def filter_by_tesisarea(request):
    select_term = request.GET.get('select', '')

    if select_term:
        tesis = Tesis.objects.filter(
            Q(area__areaname__icontains=select_term) |
            Q(area2__areaname__icontains=select_term)
        )
    else:
        tesis = Tesis.objects.all()

     # Paginación
    paginator = Paginator(tesis, 5)  # Muestra 10 libros por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    areas = Area.objects.distinct()

    context = {
        'tesis': tesis,
        'areas': areas,
        'page_obj': page_obj,
        'selected_area': select_term
    }
    return render(request, 'thesis/thesisIndex.html', context)

def filter_by_university(request):
    select_term = request.GET.get('select', '')

    if select_term:
        tesis = Tesis.objects.filter(universidad__university_name__icontains=select_term)
    else:
        tesis = Tesis.objects.all()

        universities = Universidad.objects.distinct()

    context = {
        'tesis': tesis,
        'universities': universities
    }
    return render(request, 'thesis/index.html', context)


def home(request):
    publicities = Publicity.objects.all()
    context = {
        'publicities': publicities,
        }
    return render(request, 'inicio/home.html',context)

@login_required
def books(request):
    return render(request, 'book/index.html')


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)

def exit(request):
    logout(request)
    return redirect('home')


@login_required
def magazine(request):
    magazines = Magazine.objects.all()
    context= {
         'magazines' : magazines,
    }
    return render(request, 'magazine/index.html',context)

"""def magazineDetail(request):
    magazines = Magazine.objects.all()
    context= {
         'magazines' : magazines,
    }
    return render(request, 'magazine/index2.html',context)"""


def viewMagazine(request, id ):
    magazines = Magazine.objects.get(id=id)
    context = {
        'magazines': magazines
    }
    return render(request, 'magazine/index2.html', context)


@login_required
def add_to_favorites(request, item_type, item_id):
    if item_type == 'book':
        item = get_object_or_404(Book, id=item_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, book=item, thesis=None)
    elif item_type == 'tesis':
        item = get_object_or_404(Tesis, id=item_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, thesis=item, book=None)
    else:
        return JsonResponse({'status': 'Error', 'message': 'Tipo de ítem no válido.'})

    if created:
        return JsonResponse({'status': 'Success', 'message': f'{item.title} ha sido añadido a tus favoritos.'})
    else:
        return JsonResponse({'status': 'Info', 'message': f'{item.title} ya está en tu lista de favoritos.'})



@login_required
def desktop(request):
    return render(request, 'desktop/myFavourites.html')


"""@login_required
def my_list(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    context = {
        'favorites': favorites,
    }
    return render(request, 'myFavourites.html', context)"""




@login_required
def delete_favorite(request, id):
    if request.method == "POST":
        print("Request method is POST")
        try:
            # Intenta obtener el objeto Favorite correspondiente al id proporcionado y al usuario autenticado
            favorite = Favorite.objects.get(id=id, user=request.user)
            favorite.delete()  # Elimina el objeto si se encuentra
            print("Favorite deleted")
            return JsonResponse({"success": True})
        except Favorite.DoesNotExist:
            # Maneja el caso en que el objeto Favorite no existe
            print("Favorite not found")
            return JsonResponse({"success": False, "error": "Favorite not found"})
    else:
        # Maneja el caso en que el método de solicitud no es POST
        print("Invalid request method")
        return JsonResponse({"success": False, "error": "Invalid request"})


@login_required
def article(request):
    articles = Article.objects.all()
    areas = Area.objects.all()
    context = {
        'articles': articles,
        'areas': areas,
    }
    return render(request, 'article/indexarticle.html', context)

def get_campos(request, area_id):
    campos = list(Campo.objects.filter(area_id=area_id).values('id', 'campoName'))
    return JsonResponse({'campos': campos})





def filter_by_articleArea(request):
    select_term = request.GET.get('select', '')

    if select_term:
        articles = Article.objects.filter(
            Q(articleArea__areaname__icontains=select_term) |
            Q(articleCampo__campoName__icontains=select_term)
        )
    else:
        articles = Article.objects.all()

    areasA = Area.objects.distinct()

    context = {
        'articles': articles,
        'areasA': areasA,
        'selected_area': select_term  # Para mantener el área seleccionada en el formulario
    }
    return render(request, 'article/indexarticle.html', context)

def filter_by_articleCampo(request):
    select_term = request.GET.get('select', '')

    if select_term:
        articles = Article.objects.filter(articleCampo__campoName__icontains=select_term)
    else:
        articles = Article.objects.all()

    campos = Campo.objects.distinct()

    context = {
        'articles': articles,
        'campos': campos,
        'selected_area': select_term
    }
    return render(request, 'article/indexarticle.html', context)


#Vista modals

def book_modal(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/detailBook.html', {'book': book})


def thesis_modal(request, tesis_id):
    tesis = get_object_or_404(Tesis, id=tesis_id)
    return render(request, "thesis/detailThesis.html", {'tesis': tesis})


def article_modal(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, "article/indexarticle.html", {'article': article})


@login_required
def slider_view(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    print(favorites)  # Verifica que se están obteniendo los favoritos

    context = {
        'favorites': favorites,
    }
    return render(request, 'desktop/myFavourites.html', context)



def delete_favorite(request, favorite_id):
    favorite = get_object_or_404(Favorite, id=favorite_id, user=request.user)
    favorite.delete()
    return redirect('mis-favoritos')  # Redirige a la vista después de eliminar




def book_modal_favourites(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    try:
        return FileResponse(open(book.files.path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()



def summarize_pdf(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    summary = generate_summary(book.files.path)
    return JsonResponse({'summary': summary})


def generate_summary(pdf_path):
    try:
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            text = ''
            start_index = -1

            # Extraer el texto de todas las páginas primero
            for page in reader.pages:
                text += page.extract_text()

            # Buscar el índice donde comienza "Chapter 1" o "Capítulo 1"
            keywords = ["Chapter 1", "Capítulo 1"]
            for keyword in keywords:
                start_index = text.find(keyword)
                if start_index != -1:
                    break

            # Si se encuentra el capítulo, tomar el texto desde allí
            if start_index != -1:
                summary = text[start_index:start_index + 1200]
            else:
                # Si no se encuentra el capítulo, tomar los primeros 1200 caracteres como fallback
                summary = text[:1200]

            return summary
    except Exception as e:
        return "Error al leer el PDF: " + str(e)