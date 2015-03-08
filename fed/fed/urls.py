from django.conf.urls import patterns, include, url
#from django.contrib import admin                                                                                                                   m django.conf.urls import handler404, handler500
from fomc import views
from views import index_page

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', static_serve, kwargs={
    #        'path': 'index.html', 'document_root': settings.STATIC_URL}),
    url(r'^$', index_page),
    url(r'^fed/fomc/', include('fomc.urls'))
)

handler404 = views.error404
handler500 = views.error500                                                                     
