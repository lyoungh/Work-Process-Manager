from django.contrib import admin
from .models import Work, Issue, WorkStatus, IssueStatus, Employee

# Register your models here.
admin.site.register(Work)
admin.site.register(Issue)
admin.site.register(WorkStatus)
admin.site.register(IssueStatus)
admin.site.register(Employee)
