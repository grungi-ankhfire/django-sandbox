from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^plot/$', views.BokehView.as_view(), name='bokeh-plot'),
]
