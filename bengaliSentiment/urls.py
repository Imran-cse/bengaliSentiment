from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('lexicon.urls')),
    path('lexicon/', include('lexicon.urls')),
    path('admin/', admin.site.urls),
]
