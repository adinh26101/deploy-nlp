from django.urls import path
from comment_classification.views import cmt_detect, getRating, getRatingNan, aboutUs, aboutProject

urlpatterns = [
    path('', cmt_detect, name='cmt_detect'),
    path('getRating/<comment>', getRating, name='getRating'),
    path('getRating/', getRatingNan, name='getRatingNan'),
    path('aboutUs/', aboutUs, name='aboutUs'),
    path('aboutProject/', aboutProject, name='aboutProject'),
]