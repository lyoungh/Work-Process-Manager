from django.db import models


# Create your models here.
class Work(models.Model):
    manager = models.CharField(max_length=10)
    supporter = models.CharField(max_length=10)
    work = models.TextField()
    status = models.CharField(max_length=10)
    start_date = models.DateField()
    expected_end_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return "%s: %s" % (self.manager, self.work)


class Issue(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    content = models.TextField(null=True)
    status = models.CharField(max_length=10, default="분석")
    replay = models.TextField(null=True)
    cause = models.TextField(null=True)
    solution = models.TextField(null=True)
