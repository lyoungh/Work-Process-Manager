from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, TemplateView
from .models import Work, Issue, WorkStatus, Employee, MyUser
from .forms import WorkForm, IssueForm
from django.views.generic.edit import FormMixin


# Create your views here.
class MainView(LoginRequiredMixin, ListView, FormMixin):
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


class SearchView(LoginRequiredMixin, ListView):
    template_name = 'main/main.html'
    model = Work

    def get_queryset(self):
        self.manager = self.kwargs['manager']
        self.status = self.kwargs['status']
        self.contents = self.kwargs['contents']
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


class SearchNoConView(LoginRequiredMixin, ListView):
    template_name = 'main/main.html'
    model = Work

    def get_queryset(self):
        self.manager = self.kwargs['manager']
        self.status = self.kwargs['status']

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


class SearchManView(LoginRequiredMixin, ListView):
    template_name = 'main/main.html'
    model = Work

    def get_queryset(self):
        return Work.objects.filter(manager__name__contains=self.kwargs['query'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        context['status'] = WorkStatus.objects.all()
        context['employee'] = Employee.objects.all()
        context['manager_query'] = self.kwargs['query']
        return context


class SearchStatusView(LoginRequiredMixin, ListView):
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


class CreateWorkView(LoginRequiredMixin, CreateView):
    model = Work
    form_class = WorkForm
    template_name = 'main/work_form.html'

    def form_valid(self, form):
        user = get_object_or_404(MyUser, pk=self.request.POST['manager'])
        print(self.request.user)
        if self.request.user != user:
            raise PermissionDenied
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            user = get_object_or_404(MyUser, name=self.request.user)
            form = self.form_class(initial={'manager': user})
            # print(Work.objects.get(pk=self.kwargs['pk']))
            context['form'] = form
            # context['manager'] = MyUser.objects.get(username=self.request.user)

        return context

    def get_success_url(self):
        return reverse('index')


class CreateIssueView(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = Issue
    form_class = IssueForm
    template_name = 'main/issue_form.html'

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        user = get_object_or_404(MyUser, pk=self.request.POST['manager'])
        if self.request.user != user.name:
            raise PermissionDenied
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'GET':
            form = self.form_class(initial={'work': Work.objects.get(pk=self.kwargs['work'])})
            # print(Work.objects.get(pk=self.kwargs['pk']))
            context['form'] = form
            context['work'] = Work.objects.get(pk=self.kwargs['work'])

        return context


class UpdateWorkView(PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = 'main.change_work'
    model = Work
    form_class = WorkForm
    template_name = 'main/work_update_form.html'

    def get_success_url(self):
        return reverse('index')


class UpdateIssueView(PermissionRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = 'main.change_Issue'
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


class DetailIssueView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = 'main/issue_detail.html'


@permission_required('main.delete_work', raise_exception=True)
def delete_work(request, id):
    if request.method == "GET":
        work = Work.objects.get(pk=id)
        work.delete()
        return redirect('/')


@permission_required('main.delete_issue', raise_exception=True)
def delete_issue(request, id):
    if request.method == "GET":
        issue = Issue.objects.get(pk=id)
        issue.delete()
        return redirect('/')
