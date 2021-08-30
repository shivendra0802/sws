from django.shortcuts import render
import json
import requests
from elastic.models import Elasticdemo
from .documents import *
from . serializers import *
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from  django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,

)



def generate_random_data():
    # url = 'https://newsapi.org/v2/everything?q=apple&from=2021-04-23&to=2021-04-23&sortBy=popularity&apiKey=827705eea42e455cba8bf4afafc7da90'
    url = 'https://api.stackexchange.com/'
    r = requests.get(url)
    payload = json.loads(r.text)
    count = 1
    for data in payload.get('articles'):
        print(count)
        ElasticDemo.objects.create(
            title = data.get('title'),
            content = data.get('description')
        )

def index(request):
    generate_random_data()
    return JsonResponse({'status' : 200})



# Create your views here.
class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer

    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,

    ]
    
    search_fields = ('title', 'content')
    multi_match_search_fields = ('title', 'content')
    filter_fields = {
        'title' : 'title',
        'content': 'content',
    }
