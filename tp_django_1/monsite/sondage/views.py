from django.shortcuts import render
from django.http import HttpResponse
from sondage.models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '<br>'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("Voici la question numéro %s." % question_id)

def results(request, question_id):
    response = "Voici les votes de la question numéro %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vous votez pour la question numéro %s." % question_id)
