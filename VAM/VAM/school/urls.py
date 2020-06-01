from django.conf.urls import  include, url
from django.contrib import admin

from django.conf.urls.static import static

from django.conf import settings

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
     url(r'^$', schema_view)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
