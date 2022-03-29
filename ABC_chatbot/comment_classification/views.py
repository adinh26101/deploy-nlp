from django.shortcuts import render
from django.http import HttpResponse
import pickle5 as pickle
import numpy as np
from underthesea import word_tokenize
# Create your views here.

# load dictionary
with open('static/dictionary.txt', 'rb') as f:
    dictionary = pickle.load(f)

def encoder(sentence):
    words=word_tokenize(sentence)
    onehot_vector=np.zeros(len(dictionary))
    for w in words:
        for i,word in enumerate(dictionary):
            if word==w:
                onehot_vector[i]+=1
    return onehot_vector

# load model Dtree
modelDT = pickle.load(open('static/dt.txt', 'rb'))

def cmt_detect(request):
    return render(request, 'cmt_detect_v1.html')

def getRating(request, comment):
    if comment == "":
        return HttpResponse(0)
    else:
        rating = modelDT.predict(encoder(comment).reshape(1,-1))[0]
        return HttpResponse(rating)