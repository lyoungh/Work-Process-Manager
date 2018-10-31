from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .models import Work, Issue, WorkStatus, IssueStatus, Employee, MyUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Work)
admin.site.register(Issue)
admin.site.register(WorkStatus)
admin.site.register(IssueStatus)
admin.site.register(Employee)

class UserCreationFormExtended(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(label=_("이름"), max_length=20)

UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'fields': ('name', 'username', 'password1', 'password2', 'user_permissions', 'is_staff', 'is_active', 'is_superuser')
    }),
)


admin.site.register(MyUser, UserAdmin)
