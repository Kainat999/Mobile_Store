from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request, 'login.html')
def Dash_board(request):
    return render(request, 'Dashboard.html')    
def mobile_status(request):
    return render(request, 'Ad_rm_status.html')
def order_status(request):
    return render(request, 'list_order.html')    