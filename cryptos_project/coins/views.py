from django.shortcuts import render

# Create your views here.
#! 5.) here we should define index function, that will be a root for coins app

def index(request): # this func gets a request object as an argument
    return render(request, 'index.html', context={'text': 'Hello world'}) # this func will return the result of render func; 
    # request - 1st argument'; 
    # index.html - renderred template, 
    # context's key - text we will use in renderred template - HTML file - index.html to get the value - Hello world