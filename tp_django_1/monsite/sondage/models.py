from django.db import models

# Création de models.
# Les attributs sont des models.

class Question(models.Model):
    #Charfield = Varchar
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date de publication')

class Choice(models.Model):
    #vote = Champ int integer
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
