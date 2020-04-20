from django.urls import path

from main import views
                             
app_name = "main"  

urlpatterns = [
    path('login',views.user_login, name="user_login"),
    path('logout',views.user_logout, name="user_logout"),
    path('signup',views.user_signup, name="user_signup"),
    path('index',views.index, name="index"),
    path('profile', views.profile, name="profile"),
    path('quote', views.quote, name="quote"),
    path('myPlan', views.myPlan, name="myPlan"),
    path('purchase', views.purchase, name="purchase")
]