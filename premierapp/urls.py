from django.conf.urls import include, url
from . import views

urlpatterns = [
	#url(r'^hello/', 'premierapp.views.hello', name = 'hello'),
	url(r'^hello/', views.hello, name = 'hello'),
	url(r'^$', views.post_list, name='post_list'),
	url(r'^Mon_CV.html', views.mon_cv, name='mon_cv'),
]
