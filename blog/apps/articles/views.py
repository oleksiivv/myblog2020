from django.shortcuts import render
from .models import Article,Comment, Message
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
def index(request):
    latestList=Article.objects.order_by("-publicationDate")
    return render(request,"articles/list.html",{"list":latestList})
def detail(request,articleId):
    try:
        a=Article.objects.get(id=articleId)
    except:
        raise Http404("Not found")

    latestComments=a.comment_set.order_by("-id")
    return render(request,"articles/detail.html",{'article':a,"latestComments":latestComments})

def leaveCom(request,articleId):
    try:
        a=Article.objects.get(id=articleId)
    except:
        raise Http404("Not found")

    a.comment_set.create(authorName=request.POST["name"],content=request.POST["text"],pubDate=timezone.now())
    return HttpResponseRedirect(reverse('articles:detail',args=(a.id,)))
#def addArticle(request):
#    a=Article(articleTitle=request.POST["articleT"],articleText=request.POST["cont"],publicationDate=timezone.now())
#    a.save()
#    return HttpResponseRedirect(reverse('articles:index'))
def mainPage(request):
    latestList=Article.objects.order_by("-publicationDate")[:10]
    last=Article.objects.order_by("-publicationDate")[:1]
    return render(request,"articles/main.html",{"list":latestList,"last":last})



def sendMessage(request):
    print(request.POST["nick"])
    mess=Message(nick=request.POST["nick"],message=request.POST["message"])
    mess.save()
    return HttpResponseRedirect(reverse('articles:mainPage'))
