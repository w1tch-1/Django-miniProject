from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.http import JsonResponse
from .models import Order
from .forms import OrderForm


class IndexView(ListView):
    model = Order
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm()
        return context


class OrderCreateView(CreateView):
    http_method_names = ['post',]
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        form.save()
        return JsonResponse({'success': True})
