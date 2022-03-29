from django.urls import path
from comment_classification.views import Index, GetData

urlpatterns = [
    path('', Index, name='index'),
    path('getRating', GetData, name='getRating'),
]