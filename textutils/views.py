# Created by me- Narin Ahir
from django.http import HttpResponse
from django.shortcuts import render  # --> Template render karva mate import karyu


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    print(removepunc)
    print(djtext)

    if removepunc == "on":
        punctuations = '''!.?/\|,'"-_*^%:;[]{}<>().~`'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"purpose": "Removed Punctuations", "analyzed_text": analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"purpose": "Changed To Uppercase", "analyzed_text": analyzed}
        djtext = analyzed

    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {"purpose": "Removed New Lines", "analyzed_text": analyzed}
        djtext = analyzed

    if extraspaceremove == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose": "Removed Extra Space", "analyzed_text": analyzed}
        djtext = analyzed

    if charcounter == "on":
        analyzed = len(djtext)
        params = {"purpose": "Character is Counted", "analyzed_text": analyzed}
        djtext = analyzed

    if (removepunc != "on" and fullcaps != "on" and newlineremove != "on"
            and extraspaceremove != "on" and charcounter != "on"):
        return render(request, "error.html")

    return render(request, 'analyze.html', params)
