from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Question
from .forms import RadioForm
from django.db.models import F


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'pollingapps/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    CHOICES_1 = []
    for choice in question.choice_set.all():
        CHOICES_1.append((choice.id, choice.choice_text))
    #form = RadioForm(CHOICES=CHOICES_1)
    form = RadioForm()
    form.fields['choose_occupation'].choices = CHOICES_1
    #form.choices = CHOICES_1
    # print(form.choices)
    context = {'RadioForm': form, 'question': question}
    return render(request, 'pollingapps/detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, "pollingapps/results.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(request.POST)
    selected_choice = question.choice_set.get(id=request.POST["choose_occupation"])
    print(selected_choice)
    selected_choice.votes += 1
    selected_choice.save()
    return redirect('pollingapps:results', question_id=question.id)
