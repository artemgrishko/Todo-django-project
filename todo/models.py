from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name='tasks')
