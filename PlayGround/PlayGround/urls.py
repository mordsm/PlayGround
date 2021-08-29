"""PlayGround URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
import sys , os

from observer import views
from django.views.generic import TemplateView
print (os.getcwd())
sys.path.append(".")
sys.path.append(os.path.realpath('.'))

print (os.getcwd())
app_name = 'observer'



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("gtd.urls")),  # add this line
    path('', views.detail, name='index'),
    path('<int:data_id>/', views.detail, name='detail'),
    path('template/', views.template, name='template'),
    path('thanks/', TemplateView.as_view(template_name="thanks.html"), name='thanks'),
]

