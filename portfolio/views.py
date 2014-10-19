from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from portfolio.models import Art, Portfolio

class Portfolios(ListView):

    model = Portfolio

    def get_context_data(self, **kwargs):
        context = super(Portfolios, self).get_context_data(**kwargs)
        context['foo'] = 42
        return context

class Home(TemplateView):
    template_name = "home.html"

