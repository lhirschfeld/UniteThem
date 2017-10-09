from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Fan
from datetime import datetime
def index(request):
    return HttpResponse(loader.get_template('quiz/index.html').render())

def new(request):

    if request.method == "GET":
        name = request.GET.get('name')
        email = request.GET.get('email')
        message = request.GET.get('message')
        form = request.GET.get('form')
        oath = request.GET.get('oath')
        ally = request.GET.get('ally')

        if not message:
            message = "None."
        Fan.objects.create(name = name,
                           email = email,
                           message = message,
                           form = form,
                           oath = oath,
                           ally = ally)
        users = Fan.objects.all()
        pop = len(users)
        if pop > 5:
            oldest = users[0]
            others = users[1:]
            bestMatch = None
            bestFactor = -1
            for user in others:
                factor = 0
                if user.form == oldest.form:
                    factor += 1
                if user.oath == oldest.oath:
                    factor += 1
                if user.ally == oldest.ally:
                    factor += 1
                if factor > bestFactor:
                    bestFactor = factor
                    bestMatch = user
            print(bestFactor)
            oldest.sendEmail(bestMatch.email)
            bestMatch.sendEmail(oldest.email)
            oldest.delete()
            bestMatch.delete()

        return HttpResponse("")
