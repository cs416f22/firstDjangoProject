from django.shortcuts import render


# This method renders an html page using the hello.html, which is in the template directory context is a dictionary
# that is passed to the template (i.e., hello.html) to be able to use the carried information there
def hello(request, my_name):
    context = {
        'name': my_name,
        'last_name': 'Doe',
        'states': ['CT', 'MA', 'NY']
    }
    return render(request, 'hello.html', context)


# This function takes request as a parameter and in turn returns an HttpResponse as the content of the page
# Each view you write is responsible for instantiating, populating, and returning an HttpResponse.
def goodbye(request):
    return render(request, 'goodbye.html')

