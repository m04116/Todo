from django.conf.urls import url

from .views import DetailView, IndexView, done


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^task/(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail_todo'),
    url(r'^mask/(?P<task_id>[0-9]+)/$', done, name='done'),

]
