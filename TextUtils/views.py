# # I have self created this file.
from django.http import HttpResponse
from django.shortcuts import render 


def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("<a href='/'>back</a> <br><br>Hello Brother this is about page ")

def contact(request):
    return HttpResponse("<a href='/'>back</a> <br><br>Hello Brother this is contact page ")

def analyzetext(request):
    # get the text.
    text_ = request.POST.get('text', 'default')
    # print(text_)
    removepunc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    intial_no_char = len(text_)

    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in text_:
            if char not in punctuations:
                analyzed = analyzed + char   
        text_ = analyzed
        
    if uppercase == 'on':
        analyzed = text_
        analyzed = ""
        for char in text_:
            analyzed = analyzed + char
        analyzed = analyzed.upper()
        text_ = analyzed
        
    if newlineremover== "on":
        analyzed = ""
        for char in text_:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        text_=analyzed
        text_ = analyzed
        

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(text_):
            if not (text_[index-1] == " " and text_[index] == " "):
                analyzed = analyzed + char       
        text_ = analyzed
        text_ = analyzed
        
    
    if(removepunc != 'on' and uppercase != 'on'and newlineremover!= "on" and extraspaceremover != "on"):
        return HttpResponse("Please select a option..!")
    
    final_no_char = len(text_)
    removed_no_char = intial_no_char-final_no_char
    
    params = {'intial_no_char':intial_no_char,'removed_no_char':removed_no_char,'final_no_char':final_no_char,'analyze_text':text_}

    return render(request,'analyzetext.html', params)
          
          
          
          
