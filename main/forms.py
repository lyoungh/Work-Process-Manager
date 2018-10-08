from django import forms
from .models import Work


# class WorkForm(forms.Form):
#     manager = forms.CharField(label="담당자명", max_length=10)
#     supporter = forms.CharField(label="업무협조", max_length=10)
#     work = forms.CharField(label="업무 내용", widget=forms.Textarea)
#     status = forms.CharField(label="업무 상태", max_length=10)
#     start_date = forms.DateField(label="시작일")
#     expected_end_date = forms.DateField(label="종료 예정일")
#     end_date = forms.DateField(label="종료일")


class WorkForm(forms.ModelForm):
    end_date = forms.DateField(label="종료일", required=False)

    class Meta:
        model = Work
        fields = '__all__'

        status_CHOICE = (
            ('Planning', 'Planning'),
            ('Doing', 'Doing'),
            ('Done', 'Done'),
            ('Holding', 'Holding'),
            ('Delay', 'Delay'),
            ('Expired', 'Expired'),
        )
        widgets = {
            'manager': forms.TextInput(attrs={'class': 'form-control'}),
            'supporter': forms.TextInput(attrs={'class': 'form-control'}),
            'work': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=status_CHOICE, attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'expected_end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'manager': '관리자',
            'supporter': '업무 협조',
            'work': "업무 내용",
            'status': "업무 상태",
            'start_date': "시작일",
            'expected_end_date': "종료 예정일",
            'end_date': "종료일",
        }


class IssueForm(forms.ModelForm):
    end_date = forms.DateField(label="종료일", required=False)

    class Meta:
        model = Work
        fields = '__all__'

        status_CHOICE = (
            ('Planning', 'Planning'),
            ('Doing', 'Doing'),
            ('Done', 'Done'),
            ('Holding', 'Holding'),
            ('Delay', 'Delay'),
            ('Expired', 'Expired'),
        )
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'replay': forms.Textarea(attrs={'class': 'form-control'}),
            'cause': forms.Textarea(attrs={'class': 'form-control'}),
            'solution': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=status_CHOICE, attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'expected_end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
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
