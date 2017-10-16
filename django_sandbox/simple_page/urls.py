from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^view/$', views.SimpleView.as_view(), name='simple-view'),
    url(r'^template-view/$',
        views.SimpleTemplateView.as_view(),
        name='simple-template-view'),
]
