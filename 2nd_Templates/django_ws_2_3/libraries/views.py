from django.shortcuts import render
import requests



# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    API_KEY = "ttbqjqtktnf1410001"
    API_URL = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={API_KEY}&QueryType=ItemNewSpecial&MaxResults=10&start=1&SearchTarget=Book&output=JS&Version=20131101"
    
    response = requests.get(API_URL).json()
    lst = []
    
    for s in response["item"]:
        dict_b = {
            "제목" : s["title"],
            "저자" : s["author"],
        }
        lst.append(dict_b)
    context = {
        "book" : lst
    }

    return render(request, "recommend.html", context)