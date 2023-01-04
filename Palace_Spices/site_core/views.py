from django.shortcuts import render

# Create your views here.

# define a view to render the homepage
def home_page(request):
    return render(request, "home_page.html", {})
