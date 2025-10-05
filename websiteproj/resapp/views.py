from django.shortcuts import render
def p1(request):
    return render(request,'Entrance.html')
def p2(request):
    return render(request,'Menu.html')
def p3(request):
    return render(request,'Adminstration.html')
def p4(request):
    return render(request,'Contact.html')
