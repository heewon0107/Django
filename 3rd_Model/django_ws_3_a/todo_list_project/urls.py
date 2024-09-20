from django.contrib import admin
from django.urls import path, include
# from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # todo 앱과 관련된 기능은 todos/ 경로를 통함
    # todos 앱의 urls.py 에 있는 url include
    path('todos/', include("todos.urls")),

    path("accounts/", include("accounts.urls")),
]