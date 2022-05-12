from django.shortcuts import render
from django.http import HttpResponse
import pickle
import json
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
modelDT_rt = pickle.load(open('static/dt_rt.txt', 'rb'))
modelDT_shop = pickle.load(open('static/dt_shop.txt', 'rb'))
modelDT_dvvc = pickle.load(open('static/dt_dvvc.txt', 'rb'))
modelDT_sp = pickle.load(open('static/dt_sp.txt', 'rb'))

def cmt_detect(request):
    return render(request, 'cmt_detect_v2.html')

def aboutUs(request):
    return render(request, 'about_us.html')

def aboutProject(request):
    return render(request, 'about_project.html')

def getRating(request, comment):
    data = {
        "rating": 0,
        "shop": 0,
        "dvvc": 0,
        "sp": 0
    }
    if comment == "":
        return HttpResponse(str(data))
    else:
        data["rating"] = int(modelDT_rt.predict(encoder(comment).reshape(1,-1))[0])
        data["shop"] = int(modelDT_shop.predict(encoder(comment).reshape(1,-1))[0])
        data["dvvc"] = int(modelDT_dvvc.predict(encoder(comment).reshape(1,-1))[0])
        data["sp"] = int(modelDT_sp.predict(encoder(comment).reshape(1,-1))[0])
        return HttpResponse(json.dumps(data))

def getRatingNan(request):
    data = {
        "rating": 0,
        "shop": 0,
        "dvvc": 0,
        "sp": 0
    }
    return HttpResponse(json.dumps(data))