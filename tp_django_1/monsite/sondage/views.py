from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.template import loader


def index(request):
    # return HttpResponse("Bienvenue à l'index de notre sondage")
    latest_q_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': latest_q_list}
    return render(request, 'sondage/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("La question n'existe pas !")
    return render(request, 'sondage/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'sondage/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'sondage/detail.html', {'question':question, 'error_message':'Vous devez choisir !'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('sondage:results', args=(question_id,)))
