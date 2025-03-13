from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import unicodedata
from django.db.models.functions import Lower

#Area model and logic
class Area(models.Model):
    areaname = models.TextField(max_length=100, verbose_name='area')
    
    def __str__(self):
        return self.areaname
    
#Book logic and model

def normalize_title(value):
    # Elimina las tildes y convierte a minúsculas
    normalized_value = unicodedata.normalize('NFKD', value).encode('ASCII', 'ignore').decode('ASCII').lower()
    return normalized_value

def validate_unique_title(value):
    normalized_value = normalize_title(value)
    if Book.objects.annotate(normalized_codLib=Lower('codLib')).filter(normalized_codLib=normalized_value).exists():
        raise ValidationError(f'El código de libro "{value}" ya está registrado.')

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="título")
    author = models.CharField(max_length=200, verbose_name="autor")
    edition = models.CharField(max_length=200, verbose_name="editionBook",null=True)
    codLib = models.CharField(max_length=200, verbose_name="codLib", unique=True, validators=[validate_unique_title], null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, related_name='books_primary')
    area2 = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True, related_name='books_secondary')
    publish_date = models.DateField(verbose_name="fecha de publicación", null=True)
    editorial = models.CharField(max_length=100, verbose_name="editorial")
    pages = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="páginas")
    description = models.TextField(max_length=1200, verbose_name="descripción")
    kword = models.CharField(max_length=100, verbose_name='palabra clave', null=True)
    files = models.FileField(upload_to="pdfs", verbose_name="archivos", max_length=1000)
    images = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="imágenes", max_length=1000)

    def __str__(self):
        return self.title

#Campo model and logic
class Campo(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE,null=True,related_name='campo_primary')
    campoName = models.TextField(max_length=200, verbose_name='campo',null=True)

    def __str__(self):
        return self.campoName


#University model and logic
class Universidad(models.Model):
    universityName = models.TextField(max_length=200, verbose_name='university')

    def __str__(self):
        return self.universityName

#Tesis model and logic

def normalize_titleThesis(value):
    # Elimina las tildes y convierte a minúsculas
    normalized_value = unicodedata.normalize('NFKD', value).encode('ASCII', 'ignore').decode('ASCII').lower()
    return normalized_value

def validate_unique_titleThesis(value):
    normalized_value = normalize_titleThesis(value)
    if Book.objects.annotate(normalized_codThesis=Lower('codThesis')).filter(normalized_codLib=normalized_value).exists():
        raise ValidationError(f'El código de tesis "{value}" ya está registrado.')
class Tesis(models.Model):
    title = models.TextField(max_length=200, verbose_name="title")
    author = models.TextField(max_length=100, verbose_name="author")
    edition = models.CharField(max_length=200, verbose_name="editionThesis",null=True)
    codThesis = models.CharField(max_length=200, verbose_name="codthesis", unique=True, validators=[validate_unique_titleThesis], null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE,null=True,related_name='library_primary')
    area2 = models.ForeignKey(Area, on_delete=models.CASCADE,null=True,blank=True,related_name='library_secondary')
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE,null=True,related_name='campo_name')
    publish_date = models.DateField(verbose_name="publish_date",null=True)
    universidad = models.ForeignKey(Universidad,max_length=200, on_delete=models.CASCADE,blank=True,related_name='library_university')
    pages = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="pages")
    description = models.TextField(max_length=1200, verbose_name="description")
    kword = models.CharField(max_length=100, verbose_name='kword',null=True)
    files = models.FileField(upload_to="pdfs",verbose_name="files",max_length=1000)
    images = models.ImageField(upload_to="logos", null=True, blank=True,verbose_name="images",max_length=1000)

    
    def __str__(self):
        return self.title

#Publicity logic and model
class Publicity(models.Model):
    img = models.ImageField(upload_to="flayer", null=True, blank=True, verbose_name="img", max_length=1000)
    span = models.TextField(verbose_name="span")

    def __str__(self):
        return self.span

#Magazine Logic and model
class Magazine(models.Model):
    magazineName = models.TextField(verbose_name='magazineName')
    magazineArea = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, related_name='magazineArea')
    files = models.FileField(upload_to="pdfm",verbose_name="magazineFiles",max_length=1000)
    images = models.ImageField(upload_to="logosm", null=True, blank=True,verbose_name="magazineImages",max_length=1000)

    def __str__(self):
        return self.magazineName

#Favorite Logic and model
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    thesis = models.ForeignKey(Tesis, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        parts = [f"{self.user.username}"]
        if self.book:
            parts.append(f" - {self.book.title}")
        if self.thesis:
            parts.append(f" - {self.thesis.title}")
        return ' '.join(parts)

#Article model and logic

def normalize_titleArticle(value):
    # Elimina las tildes y convierte a minúsculas
    normalized_value = unicodedata.normalize('NFKD', value).encode('ASCII', 'ignore').decode('ASCII').lower()
    return normalized_value

def validate_unique_titleArticle(value):
    normalized_value = normalize_titleArticle(value)
    if Article.objects.annotate(normalized_codLib=Lower('codLib')).filter(normalized_codArticle=normalized_value).exists():
        raise ValidationError(f'El código de artículo "{value}" ya está registrado.')

class Article(models.Model):
    articleTitle = models.TextField(max_length=200, verbose_name="articleTitle")
    articleAuthor = models.TextField(max_length=100, verbose_name="articleAuthor")
    codArticle = models.CharField(max_length=200, verbose_name="codArticle", unique=True, validators=[validate_unique_titleArticle], null=True)
    articleArea = models.ForeignKey(Area, on_delete=models.CASCADE,null=True,related_name='article_primary')
    articleArea2 = models.ForeignKey(Area, on_delete=models.CASCADE,null=True,blank=True,related_name='article_secondary')
    articleCampo = models.ForeignKey(Campo, on_delete=models.CASCADE,null=True,related_name='articles')
    articlePublish_date = models.DateField(verbose_name="publish_date",null=True)
    articleUniversidad = models.ForeignKey(Universidad,max_length=100, on_delete=models.CASCADE,blank=True,related_name='article_university', null=True)
    articlePages = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="pages")
    articleDescription = models.TextField(max_length=1200, verbose_name="description")
    articleKword = models.CharField(max_length=100, verbose_name='kword',null=True)
    articleFiles = models.FileField(upload_to="pdfs",verbose_name="files", max_length=1000)
    articleImages = models.ImageField(upload_to="logos", null=True, blank=True,verbose_name="images",max_length=1000)

    def __str__(self):
        return self.articleTitle