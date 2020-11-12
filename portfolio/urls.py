from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("",views.index,name="index"),
    path("myportfolio/",views.allportfolio,name="allportfolio"),
    path("<int:portfolio_id>",views.detail,name="detail"),
]