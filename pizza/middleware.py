from django.shortcuts import HttpResponse,render
def middle(get_response):

    print("first time running code")
    def beforafterview(request):
        print("before  view function")
        #response=get_response(request)
        response=render(request,"underconstruction.html")
        print("After  view function")
        return response
    return beforafterview    