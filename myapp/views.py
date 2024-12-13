from django.shortcuts import render
from myapp.models import News
# Create your views here.
def home(request,year,month,day):
    print(year,month,day)
    news=News.objects.filter(ndate__year=year,ndate__month=month)
    if day>0:
        news=news.filter(ndate__day=day)
    print(news.count())
    return render(request,'home.html',{'news':news.order_by('ndate'),'y':year,'m':month})

def search(request):
    q=request.GET.get('q')
    news = News.objects.filter(title__icontains=q)
    print(news.count())
    return render(request,'home.html',{'news':news.order_by('ndate')})