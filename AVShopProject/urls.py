"""AVShopProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from home_app import views as home_app_view
from ServicesApp import views as ServicesApp_view
from ContactApp import views as ContactApp_view
from AboutApp import views as AboutApp_view
from WriteUsApp import views as WriteUsApp_view
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_app_view.home_view),
    path('search_products', home_app_view.search_view,name='search_product'),
    path('product-details/<int:id>', home_app_view.prod_details_view,name='prod_details'),
    path('services/', ServicesApp_view.services_view),
    path('contact/', ContactApp_view.contact_view),
    path('contact-success', ContactApp_view.thankyou_view,name='contact-success'),
    path('about/', AboutApp_view.about_view),
    path('message/', WriteUsApp_view.message_view),
    path('suggestion-success', WriteUsApp_view.msg_thanks_view,name='suggestion-success'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
