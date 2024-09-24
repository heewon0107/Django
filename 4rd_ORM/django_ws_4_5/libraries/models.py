from django.db import models
import requests

api_key = "ttbqjqtktnf1410001"
api_url = f"https://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={api_key}&QueryType=ItemNewAll&MaxResults=10&start=1&SearchTarget=Book&output=JS&Version=20131101"


# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField(null=True, blank=True)
    category_id = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    fixed_price = models.BooleanField(null=True, blank=True)
    pub_date = models.DateField(null=True, blank=True)

    @classmethod
    def insert_data(cls):
        response = requests.get(api_url).json()

        for item in response["item"]:
            book = cls(isbn=item.get('isbn'), 
                    author = item.get("author"),
                    title = item.get("title"),
                    category_name = item.get("searchCategoryName"),
                    category_id = item.get("searchCategoryId"),
                    price = item.get("pricesales"),
                    fixed_price = item.get("fixedPrice"),
                    pub_date = item.get("pubDate"))
            book.save()    