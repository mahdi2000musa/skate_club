from django.db.models import Max
from django.shortcuts import render, get_object_or_404, redirect

from club.models import ClubMember, Banner, News


def home_page(request):
    context = {
        'banner': Banner.objects.all()
    }
    return render(request, 'home.html', context=context)

def skate(request):
    return render(request, 'kindofsk.html')


def club_member(request):

    coaches = ClubMember.objects.filter(role='C')
    players = ClubMember.objects.filter(role='P')

    context = {
        "coaches" : coaches,
        "players" : players
    }

    return render(request, 'members.html', context=context)

def show_news(request):
    news = News.objects.all().order_by('published_at')
    top_views = News.objects.aggregate(Max('views'))
    t_news = get_object_or_404(News, views=top_views['views__max'])

    context = {
        "news" : news,
        "top_views": t_news
    }

    return render(request, 'news.html', context=context)

def show_detail(request, pk):

    try:
        news = News.objects.get(id=pk)
        news.views += 1
        news.save()
        context = {
            'news': news
        }
        return render(request, 'detail.html', context=context)
    except News.DoesNotExist:
        return redirect('news')
