# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import people
# from django.template import loader

from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    return render(request, 'EzForm/index.html')

def customers(request):
    return render(request, 'EzForm/customers.html')

def vehicles(request):
    return render(request, 'EzForm/vehicles.html')

def forms(request):
    return render(request, 'EzForm/forms.html')

# def detail(request, question_id):
#     latest_person = people.objects.get(pk=1);
#     print(latest_person)
#     template = loader.get_template('polls/index.html')
#     context = {
#         'person': latest_person
#     }
#     return HttpResponse(template.render(context, request))

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
