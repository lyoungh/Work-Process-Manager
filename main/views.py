from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from .models import Work
from .forms import WorkForm
from django.views.generic.edit import FormMixin


# Create your views here.
class MainView(ListView, FormMixin):
    template_name = 'main/main.html'
    model = Work

    form_class = WorkForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        form = self.form_class(self.request.GET)
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context

    def form_valid(self, form):
        f = WorkForm(self.request.POST)
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        f.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
