from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = (request.POST.get('text','default'))
    removepunc = (request.POST.get('removepunc','off'))
    fullcaps = (request.POST.get('fullcaps','off'))
    newlineremover = (request.POST.get('newlineremover','off'))
    extraspaceremover = (request.POST.get('extraspaceremover','off'))
    analyzed=djtext
    if removepunc=='on':
        punctuations= ''':()-[]{};'"\,<>.?@#$%^&*_-`~!|'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        
    if fullcaps=='on':
        analyzed=''
        analyzed=djtext.upper()
        params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        djtext=analyzed
        
    if newlineremover=='on':
        analyzed=''
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed+=char
        params={'purpose':'Removed Extra Lines','analyzed_text':analyzed}
        djtext=analyzed
        
    if extraspaceremover=='on':
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed += char
        params={'purpose':'Removed Extra Spaces','analyzed_text':analyzed}
    
    if  extraspaceremover!='on' and extraspaceremover!='on' and newlineremover!='on' and fullcaps!='on' and removepunc!='on':
        return HttpResponse("Please select any operation and try again!! ")
    return render(request,'analyze.html',params)