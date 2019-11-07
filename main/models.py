from django.db import models
import markdown2
from django.contrib.auth.models import User

# Create your models here.
class Problem(models.Model):
    LEVEL_CHOICES = [
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Difficult')
    ]
    name = models.CharField(max_length = 256)
    description = models.TextField()
    level = models.IntegerField(choices = LEVEL_CHOICES)
#computed property
    @property
    def description_html(self):
        return markdown2.markdown(self.description)

    def __str__(self):
        return self.name

class Contest(models.Model):
    name = models.CharField(max_length = 256)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    is_private = models.BooleanField(default = False)
    problems = models.ManyToManyField('Problem')

    def __str__(self):
        return self.name

class StudentContest(models.Model):
    contest = models.ForeignKey('Contest', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.user, self.contest)

class Submission(models.Model):
    LANGUAGES = [
        (1, 'cpp'),
        (2, 'c'),
        (3, 'java'),
        (4, 'python')
    ]
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    contest = models.ForeignKey('Contest', on_delete = models.CASCADE)
    problem = models.ForeignKey('Problem', on_delete = models.CASCADE)
    score = models.IntegerField(null = True)
    createdAt = models.DateTimeField(auto_now_add = True)