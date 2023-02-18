from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_page),
    path('MobileStatus/', views.mobile_detail),
    path('MobileStatus/DropBox/', views.drop_box),
    path('MobileStatus/DropBox/OrderStatus', views.Order_status)
]
