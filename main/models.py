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
    end_date = models.DateField()
    content = models.CharField(max_length=100)
    replay = models.CharField(max_length=100)
    cause = models.CharField(max_length=100)
    solution = models.CharField(max_length=100)
