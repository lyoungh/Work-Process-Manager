from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Work, Issue
from .forms import WorkForm, IssueForm
from django.views.generic.edit import FormMixin


# Create your views here.
class MainView(ListView, FormMixin):
    template_name = 'main/main.html'
    model = Work

    form_class = WorkForm

    def get_context_data(self, **kwargs):
        form = self.form_class()
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
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


class CreateIssueView(CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'main/issue_form.html'

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            form = self.form_class(initial={'work': Work.objects.get(pk=self.kwargs['pk'])})
            print(Work.objects.get(pk=self.kwargs['pk']))
            context['form'] = form

        return context


class UpdateWorkView(UpdateView):
    model = Work
    form_class = WorkForm
    template_name = 'main/work_update_form.html'

    def get_success_url(self):
        return reverse('index')


class UpdateIssueView(UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'main/issue_update_form.html'

    def get_success_url(self):
        return reverse('index')


class DetailIssueView(DetailView):
    model = Issue
    template_name = 'main/issue_detail.html'


def delete_work(request, id):
    if request.method == "GET":
        work = Work.objects.get(pk=id)
        work.delete()
        return redirect('/')


def delete_issue(request, id):
    if request.method == "GET":
        issue = Issue.objects.get(pk=id)
        issue.delete()
        return redirect('/')
