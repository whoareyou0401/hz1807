from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r"^add_book$", create_book),
    url(r"^book$", book_api),
    url(r"^book_one$", BookApi.as_view()),
    url(r"^template_view$", HelloTemplateView.as_view()),
    url(r"^books$", MyListView.as_view()),
    url(r"^book/(?P<name>.*)", BookDetailView.as_view(), name="book")
]