from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^brands$', views.brands, name='brands'),
    url(r'^brand_goods/(?P<bid>\d+)$', views.brand_goods, name='b_goods'),
    url(r'^goods$', views.goods, name='goods'),
    url(r'^cates$', views.cates, name='cates'),
    url(r'^c_goods/(?P<cid>\d+)$', views.c_goods, name='c_goods')
]