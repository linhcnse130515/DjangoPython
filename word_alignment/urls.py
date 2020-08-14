from django.urls import path
from . import views

urlpatterns = [
    path('word_align/',views.inputFile),
    ##path('input/word_align/',views.word_align),
    path('download/',views.downloadFile)
]
