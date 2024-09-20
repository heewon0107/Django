import requests
from django.shortcuts import render

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbqjqtktnf1410001'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '10',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'title': item['title'],
            'author': item['author'],
            "rank" : item.get("bestDuration"),
            "sell" : item.get("salesPoint"),
        }
        result.append(info)
    result.sort(key = lambda x : x["sell"], reverse=True)
    print(result)
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)