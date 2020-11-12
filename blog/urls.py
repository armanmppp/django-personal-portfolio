from django.urls import path,re_path
from . import views

app_name = "blog"
urlpatterns = [
    path("",views.index,name="index"),
    path("<int:blog_id>",views.detail,name="detail"),
]