from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
     path('logout/', views.logoutUser, name="logout"),
     path('login/', views.loginPage, name="login"),
     path('register/', views.registerUser, name="register"),
    # path('edit-account/', views.editAccount, name='edit-account'),
    # path('user-account/', views.userProfile, name='user-profile'),
    # path('user-account/', views.userAccount, name='user-profile'),
]
