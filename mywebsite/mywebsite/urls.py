"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from myapp import views
from django.conf import settings  
from django.conf.urls.static import static  

  

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('myapp.urls')),
     path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('services/', views.services, name='services'),

    path('adddata/', views.adddata, name='adddata'),
    path('update_data/<id>',views.update_data,name='update_data'),
    # path('save_update_data/<id>',views.save_update_data,name='save_update_data'),
    path('delete_data/<id>',views.delete_data,name='delete_data'),
    path('contact/', views.contact, name='contact'),
    # path('gallery/', views.gallery, name='gallery'),
    path('feedback/', views.feedback, name='feedback'),
    path('feed_add/',views.feed_add,name='feed_add'),
    path('add_gallery/', views.image_request, name = "image-request")
    
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
