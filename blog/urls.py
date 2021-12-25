from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
    path('',views.frontpage, name='blogs'),
    path('<slug:slug>/',views.post_detail, name="posts")
]
