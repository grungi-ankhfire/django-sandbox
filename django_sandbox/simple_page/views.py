from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views import View


class SimpleView(View):
    def get(self, request):
        return HttpResponse('<h1>Simple View</h1>This is a view.')


class SimpleTemplateView(TemplateView):
    template_name = "simple_page/simple_template_view.html"
