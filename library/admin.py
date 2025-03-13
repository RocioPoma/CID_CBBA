from django.contrib import admin
from .models import Book, Area, Tesis, Campo, Universidad,Publicity,Magazine, Favorite,Article

class BookAdmin(admin.ModelAdmin):
    model = Book
    search_fields = ['title']

class TesisAdmin(admin.ModelAdmin):
    model = Tesis
    search_fields = ['title']

class CampoAdmin(admin.ModelAdmin):
    model = Campo
    search_fields = ['campoName']

class UniversityAdmin(admin.ModelAdmin):
    model = Universidad
    search_fields = ['universityName']

class MagazineAdmin(admin.ModelAdmin):
    model = Magazine
    search_fields = ['magazineName']

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ['title']


admin.site.register(Book,BookAdmin)
admin.site.register(Area)
admin.site.register(Tesis,TesisAdmin)
admin.site.register(Campo, CampoAdmin)
admin.site.register(Universidad, UniversityAdmin)
admin.site.register(Publicity)
admin.site.register(Magazine,MagazineAdmin)
admin.site.register(Favorite)
admin.site.register(Article,ArticleAdmin)