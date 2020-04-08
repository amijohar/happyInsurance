from django.urls import path

from main import views
                             
app_name = "main"  

urlpatterns = [
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('signup',views.user_signup)
]