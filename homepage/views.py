from django.shortcuts import render, get_object_or_404

from news.models import News
import requests

from category.models import Category

# Create your views here.
API_KEY = 'AIzaSyAYzY1vH_A9fzixHx9GMZjJ6AoNl49Fi98'
CHANNEL_ID = 'UC8eaQTAUBKj_OrNmXThrvbQ'


def get_youtube_videos(max_results=20):
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'key': API_KEY,
        'channelId': CHANNEL_ID,
        'part': 'snippet',
        'order': 'date',
        'maxResults': max_results,
        'type': 'video'
    }

    response = requests.get(url, params=params)
    data = response.json()
    videos = []
    for item in data.get('items', []):
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        thumbnail = item['snippet']['thumbnails']['high']['url']
        published = item['snippet']['publishedAt']
        videos.append({
            'video_id': video_id,
            'title': title,
            'thumbnail': thumbnail,
            'publishedAt': published,
            'url': f'https://www.youtube.com/watch?v={video_id}'
        })
    return videos


def homepage(request):
    videos = get_youtube_videos()[:4]
    news = News.objects.filter(category__name='Crime')
    categories = Category.objects.prefetch_related('news_set')
    context = {
        'news': news,
        'videos': videos,
        'categories': categories ,
    }
    return render(request, 'index.html', context)


def news_detail(request, slug):
    news = get_object_or_404(News, id=slug)
    latest_news = News.objects.filter(category_id=slug).exclude(id=news.id).order_by('-id')[:5]
    # increase view count
    news.count += 1
    news.save(update_fields=["count"])

    context = {
        'news': news,
        'latest_news': latest_news,
    }
    return render(request, "news_detail.html", context)
