from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

urlpatterns = [

    path("admin/", admin.site.urls),
    path("api/2.0/", include("api.urls"))

]
