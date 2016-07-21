from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<date>\d{4}-\d{2}-\d{2})', views.index, name='index'),
]