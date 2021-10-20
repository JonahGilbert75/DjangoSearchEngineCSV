from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


def index(request):    
        
    csv_file = "python_assesment.csv"
    csv_data= pd.read_csv(csv_file)
    data= list(csv_data.name)    
    list_data=[]    
    if request.method=="POST":
        search_data=request.POST.get('search_data')        
        for i in data:
            if str(search_data).lower() in i.lower():
                list_data.append(i)
   
    return render(request,'index.html',{'list_data':list_data[:20]})
