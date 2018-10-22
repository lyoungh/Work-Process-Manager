from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Work, Issue, WorkStatus, Employee
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
        context['status'] = WorkStatus.objects.all()
        context['employee'] = Employee.objects.all()
        return context


class SearchView(ListView):
    template_name = 'main/main.html'
    model = Work

    def get_queryset(self):
        self.manager= self.kwargs['manager']
        self.status= self.kwargs['status']
        self.contents =self.kwargs['contents']
        if self.contents == "":
            contents = ""

        if self.manager == 'all' and self.status == 'all':
            return Work.objects.filter(work__contains=self.contents)
        elif self.manager == 'all':
            return Work.objects.filter(work__contains=self.contents,
                                       status__title__contains=self.status)
        elif self.status == 'all':
            return Work.objects.filter(work__contains=self.contents,
                                       manager__name__contains=self.manager)
        else:
            return Work.objects.filter(work__contains=self.contents,
                                       manager__name__contains=self.manager,
                                       status__title__contains=self.status)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        context['status'] = WorkStatus.objects.all()
        context['employee'] = Employee.objects.all()
        if self.manager != 'all':
            context['manager_query'] = self.manager
        if self.status != 'all':
            context['status_query'] = self.status

        return context


class SearchNoConView(ListView):
    template_name = 'main/main.html'
    model = Work

    def get_queryset(self):
        self.manager= self.kwargs['manager']
        self.status= self.kwargs['status']

        if self.manager == 'all' and self.status == 'all':
            return Work.objects.all()
        elif self.manager == 'all':
            return Work.objects.filter(status__title__contains=self.status)
        elif self.status == 'all':
            return Work.objects.filter(manager__name__contains=self.manager)
        else:
            return Work.objects.filter(manager__name__contains=self.manager,
                                       status__title__contains=self.status)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        context['status'] = WorkStatus.objects.all()
        context['employee'] = Employee.objects.all()

        if self.manager != 'all':
            context['manager_query'] = self.manager
        if self.status != 'all':
            context['status_query'] = self.status
        return context


class SearchManView(ListView):
    template_name = 'main/main.html'
    model = Work

    def get_queryset(self):
        return Work.objects.filter(manager__name__contains=self.kwargs['query'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        context['status'] = WorkStatus.objects.all()
        context['employee'] = Employee.objects.all()
        context['manager_query'] =self.kwargs['query']
        return context


class SearchStatusView(ListView):
    template_name = 'main/main.html'
    model = Work

    def get_queryset(self):
        return Work.objects.filter(status__title__contains=self.kwargs['query'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        context['status'] = WorkStatus.objects.all()
        context['employee'] = Employee.objects.all()
        context['status_query'] = self.kwargs['query']
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
            form = self.form_class(initial={'work': Work.objects.get(pk=self.kwargs['work'])})
            # print(Work.objects.get(pk=self.kwargs['pk']))
            context['form'] = form
            context['work'] = Work.objects.get(pk=self.kwargs['work'])

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(Issue.objects.get(self.kwargs['pk']))
        context['work'] = Issue.objects.get(pk=self.kwargs['pk']).work
        return context

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
