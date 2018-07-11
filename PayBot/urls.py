"""PayBot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import re_path,path,include
from django.contrib.auth import views as auth_views
from payments import views
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'billerprofile', views.BillerProfileViewSet)
router.register(r'payments', views.PaymentsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    re_path(r'login/$', auth_views.login, name='login'),
    re_path(r'accounts/login/$', auth_views.login, name='login'),
    re_path(r'logout/$', auth_views.logout, name='logout'),
    re_path(r'api/hello', views.ApiEndpoint.as_view()),
    re_path(r'secret$', views.secret_page, name='secret'),
    re_path(r'signup/$', views.signup, name='signup'),
    re_path(r'home/$', views.home, name='home'),
    re_path(r'', include(router.urls)),
    re_path(r'^api-visapay/', include('rest_framework.urls',namespace='rest_framework')),
    re_path(r'billerprofile/',views.biller_profile_list),
    re_path(r'payments/',views.payments)
]
