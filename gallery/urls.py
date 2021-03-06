from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^image/(?P<image_id>\d+)/$', views.image, name='single_image'),
    url(r'^kenya/$', views.get_kenya, name='kenya'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)