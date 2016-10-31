from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from hello import views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^db', views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^flyweight/$', views.flyweight, name='flyweight'),
    url(r'^flyweight/([0-9]{3})/$', views.flyweight_num, name='fw_num'),
    url(r'^flyweight/([0-9]{3})/no/$', views.no_flyweight_num, name='nofw_num'),
    url(r'^flyweight/ordenes/$', views.ordenes, name='ordenes'),
    url(r'^flyweight/ordenes/no/$', views.ordenes_no, name='ordenes_no'),
    url(r'^flyweight/nueva_orden/$', views.nueva_orden, name='nueva_orden'),
    url(r'^flyweight/nueva_orden/([0-9]{2})/$', views.nueva_orden_num, name='nueva_orden_num'),
]
