import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wlist = fulltext.split()
    wdic = {}
    for word in wlist:
        if word in wdic:
            wdic[word] += 1
        else:
            wdic[word] = 1
    sortedwords=sorted(wdic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wlist),'sortedwords':sortedwords})

