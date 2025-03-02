from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home page Request")
    friends = ['Ram', 'Shyam', 'Mohan', 'Rohan']
    return JsonResponse(friends, safe=False)