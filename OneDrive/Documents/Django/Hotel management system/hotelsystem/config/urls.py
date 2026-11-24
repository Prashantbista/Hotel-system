"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from Hotel.views import ai_chat,home,list_client,Menu_list,book_table,delete,edit_client
from accounts.views import register,profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("Hotel.urls_api")),
    path("",home, name="home"),
    path("clients",list_client,name="client"),
    path("menu/",Menu_list,name="menu"),
    path("book_table/", book_table, name="book_table"),
    path("Hotel/delete/<int:Hotel_id>", delete, name="delete"),
    path("edit/<int:Hotel_id>/", edit_client, name="edit_client"),

    path("register/", register, name="register"),
    path("accounts/login/", auth_views.LoginView.as_view (template_name="accounts/login.html"),name="login"),
    path("accounts/logout/",auth_views.LogoutView.as_view(next_page="home"),name="logout"),
    path("accounts/profile/",profile, name="profile"),
     path("ai-chat/", ai_chat, name="ai_chat"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
