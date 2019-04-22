from django.conf.urls import url
from django.contrib import admin
from regloginapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^registration/',views.registration),
    url(r'^login/',views.login),
]
