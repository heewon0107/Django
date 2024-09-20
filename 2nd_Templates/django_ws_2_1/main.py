import requests
from pprint import pprint as print

API_KEY = "ttbqjqtktnf1410001"
API_URL = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={API_KEY}&QueryType=ItemNewSpecial&MaxResults=50&start=1&SearchTarget=Book&output=JS&Version=20131101"
params = {
    'ttbkey': API_KEY,
}

response = requests.get(API_URL).json()
dict_b = {}
lst = []
# dict_b["국제 표준 도서 번호"] : response["isbn"]
for s in response["item"]:
    dict_b["국제 표준 도서 번호"] = s["isbn"]
    dict_b["저자"] = s["author"]
    dict_b["제목"] = s["title"]
    dict_b["출간일"] = s["pubDate"]
    lst.append(dict_b)
print(lst)
           
     
# title author pubDate isbn