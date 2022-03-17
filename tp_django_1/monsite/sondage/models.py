from django.db import models
from django.utils import timezone
import datetime

# Création de models.
# Les attributs sont des models.

class Question(models.Model):
    #Charfield = Varchar
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date de publication')

    #Méthode pour print Question.objects.all()
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    #vote = Champ int integer
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

