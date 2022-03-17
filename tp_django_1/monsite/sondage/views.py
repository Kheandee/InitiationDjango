from django.shortcuts import render
from django.http import HttpResponse
from sondage.models import Question
from django.template import loader

from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('sondage/index.html')
    context = {'question_list': latest_question_list}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("Voici la question numéro %s." % question_id)

def results(request, question_id):
    response = "Voici les votes de la question numéro %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vous votez pour la question numéro %s." % question_id)