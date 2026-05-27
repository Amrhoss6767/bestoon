from django.shortcuts import render
import json
# Create your views here.

def submit_expense(request):
    print ("i am in submit expense")
    print (request.POST)

    return jsonResponse({
        "status" : "ok" ,
    }, encoder = json.JSONEncoder)
    