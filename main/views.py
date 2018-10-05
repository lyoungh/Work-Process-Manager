from django.shortcuts import render, redirect
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

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        form = self.form_class(self.request.GET)
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context
    #
    # def form_valid(self, form):
    #     query_id = self.request.REQUEST['id']
    #     print(query_id)
    #     try:
    #         work = Work.objects.get(pk=query_id)
    #     except Work.DoesNotExist:
    #         work = None
    #     f = WorkForm(self.request.POST, instance=work)
    #     # Here, we would record the user's interest using the message
    #     # passed in form.cleaned_data['message']
    #     f.save()
    #     return super().form_valid(form)


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