from django.urls import path
from . views import homePageView
from . views import HomePageView, AboutPageView



urlpatterns = [
	path("about/", AboutPageView.as_view(), name="about"),
	path("home/", HomePageView.as_view(), name="home"),
	path("", homePageView, name="testpage"),
]