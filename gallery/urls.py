from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('search', views.search_results, name='search_results'),
    url('personal', views.personal, name='personal'),
    url('image/<int:image_id>', views.image, name='single_image'),
    url('kenya', views.get_kenya, name='kenya'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)