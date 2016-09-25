from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def hello(request):
	today = datetime.datetime.now().date()
	return render(request, "myapp/templates/hello.html", {"today" : today})


def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)