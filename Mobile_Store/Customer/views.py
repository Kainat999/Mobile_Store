from django.shortcuts import render
def login_page(request):
    return render(request, 'c_login.html')
def mobile_detail(request):
    return render(request, 'm_detail.html')
def drop_box(request):
    return render(request, 'Cart_msg.html')
def Order_status(request):
    return render(request, 'Or_detail.html')            

# Create your views here.
