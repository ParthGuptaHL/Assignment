from django.contrib import admin
from django.urls import path
from translator.views import translate_text

urlpatterns = [
    path("admin/", admin.site.urls),
    path('translate/', translate_text, name='translate'), #Added URL for translate view
]
