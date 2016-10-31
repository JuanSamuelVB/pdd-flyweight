from django.contrib import admin

from .models import Greeting, SaborDeNieve, Cliente, Orden

# Register your models here.
admin.site.register(Greeting)
admin.site.register(SaborDeNieve)
admin.site.register(Cliente)
admin.site.register(Orden)
