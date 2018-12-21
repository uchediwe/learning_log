"""learning_log URL Configuration

"""
from django.contrib import admin
from django.conf.urls import include,url

app_name ="learning"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include(('learning_logs.urls',app_name), namespace='learning_logs')),
]
