
from django.contrib import admin
from django.urls import path, include
from PIL1_2324_9_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('PIL1_2324_9_app/', include('PIL1_2324_9_app.urls')),
    path('', include('PIL1_2324_9_app.urls')),
    # path('register/',views.register,name='register'),
    # path('', views.login, name='login')
 
]
# dating_app/urls.py

# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(' ', include('PIL1_2324_9_app.urls')),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)