from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class WorkStatus(models.Model):
    title = models.CharField(max_length=10)
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class IssueStatus(models.Model):
    title = models.CharField(max_length=10)
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Work(models.Model):
    manager = models.ForeignKey(MyUser, on_delete=models.SET_NULL, related_name='manager', null=True)
    supporter = models.ManyToManyField(Employee, blank=True)
    work = models.TextField()
    status = models.ForeignKey(WorkStatus, on_delete=models.SET_NULL, related_name='status', null=True)
    start_date = models.DateField(default=datetime.now, null=True)
    expected_end_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    def __str__(self):
        return "%s: %s" % (self.manager, self.work)


class Issue(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(null=True)
    content = models.TextField(null=True)
    status = models.ForeignKey(IssueStatus, on_delete=models.SET_NULL, related_name='status', null=True)
    replay = models.TextField(null=True)
    cause = models.TextField(null=True)
    solution = models.TextField(null=True)

