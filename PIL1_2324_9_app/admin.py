from django.contrib import admin
from django.apps import apps 

app = apps.get_app_config('PIL1_2324_9_app')

for model_name, model in app.models.items(): #boucle pour afficher dans la page admin les modeles creer dans l'application
 admin.site.register(model)
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# admin.site.register(User,UserAdmin)
# Register your models here.
