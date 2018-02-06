from django.conf.urls import include, url
from . import views

urlpatterns = [
	#url(r'^hello/', 'premierapp.views.hello', name = 'hello'),
	url(r'^hello/', views.hello, name = 'hello'),
	url(r'^$', views.post_list, name='post_list'),
	url(r'^Mon_CV.html', views.mon_cv, name='mon_cv'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
