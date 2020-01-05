from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    #This is the page that the website automatically loads to..
    path('', include('blog.urls')),

]
