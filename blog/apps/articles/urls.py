from django.urls import path

from . import views
app_name="articles"
urlpatterns=[
    path('',views.mainPage,name="mainPage"),
    path('articles/',views.index,name="index"),
    path('articles/<int:articleId>/',views.detail,name="detail"),
    path('articles/<int:articleId>/leaveCom',views.leaveCom,name="leaveCom"),
    path('articles/sendMessage',views.sendMessage,name="sendMessage"),


]
