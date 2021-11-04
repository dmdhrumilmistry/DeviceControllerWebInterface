from django.urls import path
from controller import views


urlpatterns = [
    path('', views.index, name='home'),
    path('update', views.update_values, name='update_values'),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),

]
