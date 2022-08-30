"""Firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Webapp import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Webapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('handleLogin',views.handleLogin,name="handleLogin"),
    path('About/',views.aboutSection ,name="About"),
    path('Services/',views.serviceSection,name="Services"),
    path('Contact/',views.contactInfo ,name="Contact"),
    path('Login/',views.loginPage,name="loginPage"),
    path('Logout/',views.logoutPage,name="logoutPage"),
    path('HomePageData/',views.homePageData,name="HomePageData"),
    path('Register/',views.registerPage,name="Register"),
    path('add_product/',views.addProduct,name="add_products"),
    path('dog_info',views.dog_info,name="dog_info"),
    path('viewDetail/<int:id>',views.viewDetail,name="viewDetail"),
    path('viewMore/<int:id>',views.viewMore,name="viewMore")



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)