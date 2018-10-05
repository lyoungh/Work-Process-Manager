from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from .models import Work
from .forms import WorkForm
from django.views.generic.edit import FormMixin


# Create your views here.
class MainView(ListView, FormMixin):
    template_name = 'main/main.html'
    model = Work

    form_class = WorkForm

    def get_context_data(self, **kwargs):
        form = self.form_class()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context


def update_work(request, id):
    if request.method == "POST":
        try:
            work = Work.objects.get(pk=id)
            print(work)
        except Work.DoesNotExist:
            work = None

        form = WorkForm(request.POST, instance=work)
        if form.is_valid():  # 폼 검증 메소드
            form.save()
            print('success')
            return redirect('/')  # url의 name을 경로대신 입력한다.
        else:
            print(form.errors)
            return redirect('/')
    else:
        return redirect('/')  # 템플릿 파일 경로 지정, 데이터 전달


class CreateWorkView(CreateView):
    model = Work
    form_class = WorkForm
    template_name = 'main/work_form.html'

    def get_success_url(self):
        return reverse('index')
