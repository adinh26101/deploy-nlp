from django.urls import path
from comment_classification.views import cmt_detect, getRating

urlpatterns = [
    path('', cmt_detect, name='cmt_detect'),
    path('getRating/<comment>', getRating, name='getRating'),
]