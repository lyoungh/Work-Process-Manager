from django import forms
from .models import Work, Issue, WorkStatus, IssueStatus, Employee


# class WorkForm(forms.Form):
#     manager = forms.CharField(label="담당자명", max_length=10)
#     supporter = forms.CharField(label="업무협조", max_length=10)
#     work = forms.CharField(label="업무 내용", widget=forms.Textarea)
#     status = forms.CharField(label="업무 상태", max_length=10)
#     start_date = forms.DateField(label="시작일")
#     expected_end_date = forms.DateField(label="종료 예정일")
#     end_date = forms.DateField(label="종료일")


class WorkForm(forms.ModelForm):
    # end_date = forms.DateField(label="종료일", required=False)
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(WorkForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['end_date'].required = False

    class Meta:
        model = Work
        fields = '__all__'

        # status_CHOICE = tuple(WorkStatus.objects.all())
        # print(tuple(WorkStatus.objects.))

        widgets = {
            'manager': forms.Select(attrs={'class': 'form-control col-md-2'}),
            'supporter': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'work': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control col-md-2'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control col-md-3', 'id':'datepicker1'}),
            'expected_end_date': forms.DateInput(attrs={'class': 'form-control col-md-3', 'id':'datepicker2'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control col-md-3', 'id':'datepicker3'}),
        }
        labels = {
            'manager': '담당자',
            'supporter': '업무 협조',
            'work': "업무 내용",
            'status': "업무 상태",
            'start_date': "시작일",
            'expected_end_date': "종료 예정일",
            'end_date': "종료일",
        }


class IssueForm(forms.ModelForm):
    # end_date = forms.DateField(label="종료일", required=False)

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(IssueForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['end_date'].required = False
        self.fields['solution'].required = False
        self.fields['replay'].required = False
        self.fields['cause'].required = False

    class Meta:
        model = Issue
        fields = '__all__'

        status_CHOICE = (
            ('분석', '분석'),
            ('해결', '해결'),
            ('보류', '보류'),
            ('공개', '공개'),
        )
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'replay': forms.Textarea(attrs={'class': 'form-control'}),
            'cause': forms.Textarea(attrs={'class': 'form-control'}),
            'solution': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control col-md-2'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control col-md-2', 'id':'datepicker1'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control col-md-2', 'id':'datepicker2'}),
        }
        labels = {
            'content': '증상',
            'replay': '재연 경로',
            'cause': "원인 분석",
            'solution': "해결 방안",
            'status': "상태",
            'start_date': "시작일",
            'end_date': "종료일",
        }
