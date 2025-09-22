from django.contrib import admin
from galeria.models import Fotografia

# Register your models here.


class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "publicado","nome", "legenda", "categoria", )
    list_display_links = ("id", "nome")
    search_fields = ("nome","legenda", "categoria")
    list_filter = ("categoria", "publicado","usuario")
    list_editable = ("publicado",)
    list_per_page = 10
admin.site.register(Fotografia, ListandoFotografias)