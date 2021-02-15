from django.urls import path
from webapp2.views import webapp2_demo_view


urlpatterns = [
    path('demo', webapp2_demo_view)
]
