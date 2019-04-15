from django.urls import path

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', admin.site.urls),
]
