from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def count(request):
    gettext = request.GET['text']
    result = len(gettext)
    # print Word frequency
    word_dict = {}
    for word in gettext:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    word_dict = sorted(word_dict.items(),key = lambda w:w[1] ,reverse = True)
    #print (word_dict)
    return render(request,'count.html',{'result':result,
                                        'text':gettext,
                                        'dict':word_dict})