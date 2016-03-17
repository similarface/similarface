from django.contrib import admin
from .models import Entry,Author,Blog,Ox
# Register your models here.

admin.site.register(Entry)

admin.site.register(Author)

admin.site.register(Blog)

admin.site.register(Ox)
