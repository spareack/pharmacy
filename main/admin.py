from django.apps import apps
from django.contrib import admin

# Получаем все приложения проекта
all_apps = apps.get_app_configs()

for app in all_apps:
    for model in app.get_models():
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass
