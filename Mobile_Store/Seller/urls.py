
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_page),
    path('Dashboard/', views.Dash_board),
    path('Dashboard/MobileStatus', views.mobile_status),
    path('Dashboard/OrderStatus', views.order_status),
]