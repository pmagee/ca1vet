from django.contrib import admin
from .models import Surgery, Animal, Vet

# Register your models here.
admin.site.register(Surgery)
admin.site.register(Animal)
admin.site.register(Vet)
