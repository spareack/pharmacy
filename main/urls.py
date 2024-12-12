import os.path

from django.conf import settings
from django.http import FileResponse
from django.urls import path

from . import views

build_path = os.path.join(settings.BASE_DIR, "build")

urlpatterns = [
    path("", views.index),
    path("logo192.png", lambda request: FileResponse(open(os.path.join(build_path, "logo192.png"), "rb"))),
    path("favicon.ico", lambda request: FileResponse(open(os.path.join(build_path, "favicon.ico"), "rb"))),
    path("manifest.json", views.manifest),
    path("get_medicines", views.get_medicines),
]
