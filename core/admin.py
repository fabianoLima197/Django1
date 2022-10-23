from django.contrib import admin
from .models import Produto, Cliente

# Register your models here.
class ProdudoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Produto, ProdudoAdmin)
admin.site.register(Cliente, ClienteAdmin)
