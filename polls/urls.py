from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(regex=r'^$', view=views.index, name='index'),
    url(regex=r'^(?P<question_id>[0-9]+)/$', view=views.detail, name='detail'),
    url(regex=r'^(?P<question_id>[0-9]+)/results/$', view=views.results, name='results'),
    url(regex=r'^(?P<question_id>[0-9]+)/vote/$', view=views.vote, name='vote'),
]
