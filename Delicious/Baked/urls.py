from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^view$', views.view, name='view'),
    url(r'^editcontact/(?P<id>\d+)/$', views.updatecontact, name='contact'),
    url(r'^delete/(?P<id>\d+)/$', views.deletecontact, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)