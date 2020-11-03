from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()

STATUS_CHOICES = (
    ('ACTIVE', 'Active'),
    ('ON_HOLD', 'On Hold'),
    ('COMPLETED', 'Completed'),
)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ('title', 'start_date',)

    def get_absolute_url(self):
        """
        Get url for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse('projects:detail', kwargs={'id': self.id})

    def __repr__(self):
        return '[{id}] - {title}'.format(id=self.id, title=self.title)

    def __str__(self):
        return self.title
