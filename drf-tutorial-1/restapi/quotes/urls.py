from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from quotes import views

urlpatterns = [
    path('quotes/', views.QuoteList.as_view()),
    path('quotes/<int:pk>/', views.QuoteDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
