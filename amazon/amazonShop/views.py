from django.shortcuts import render

def homePage(request): 
    context = {} # data send along with responce. 


    return render(request, 'amazonShop/homePage.html', context) # responce. 