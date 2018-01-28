from django.conf.urls import include, url

urlpatterns = [
	url(r'^hello/', 'premierapp.views.hello', name = 'hello'),
]
