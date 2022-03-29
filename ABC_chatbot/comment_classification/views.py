from django.shortcuts import render
from django.http import HttpResponse
# import numpy as np
# import pickle
# from underthesea import word_tokenize
# from django.contrib.staticfiles.storage import staticfiles_storage
# Create your views here.

# # load dictionary
# with open(staticfiles_storage.url('dictionary.txt'), 'r') as f:
#     dictionary = [line.rstrip('\n') for line in f]

# def encoder(sentence):
#     words=word_tokenize(sentence)
#     onehot_vector=np.zeros(len(dictionary))
#     for w in words:
#         for i,word in enumerate(dictionary):
#             if word==w:
#                 onehot_vector[i]+=1
#     return onehot_vector

# # load model Dtree
# modelDT = pickle.load(open('dt.txt', 'rb'))

def Index(request):
    return render(request, 'cmt_detect_v1.html')

def GetData(request):
    rating = np.random. randint(1,5)
    return HttpResponse(rating)