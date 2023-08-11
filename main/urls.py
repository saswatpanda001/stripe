
from django.urls import path,include
from main import views

app_name = "main_app"

urlpatterns = [
    path('', views.home,name="home"),
    path('payment', views.payment,name="pay"),
    path('confirm/<str:pk>', views.confirm,name="confirm"),
    path('profile', views.profile,name="profile"),
    path('login', views.login,name="login"),
    path('register', views.register,name="register"),
]




