"""
URL configuration for uniherse project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from post import views
import account.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('main', views.main2, name='main2'),

    path('burn_list/', views.burn_list, name='burn_list'),
    path('career_list/', views.career_list, name='career_list'),
    path('diet_list/', views.diet_list, name='diet_list'),
    path('job_list/', views.job_list, name='job_list'),
    path('love_list/', views.love_list, name='love_list'),
    path('rel_list/', views.rel_list, name='rel_list'),
    path('create/',views.write_post, name='write'),
    path('post_list/', views.counsel_post_list, name='list'),
    path('detail/<int:id>/', views.post_detail, name='post_detail'),
    path('update/<int:id>/', views.post_update, name='post_update'),
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),
    path('create_recomment/<int:id>', views.create_recomment, name="create_recomment"),
    path('jar_list/', views.jar_list, name='jar_list'),
    path('like_post/<int:id>', views.like_post, name='like_post'),
    
     path('', views.meb, name='meb'),
    path('account/login', account.views.login_view, name="login"),
    path('account/logout', account.views.logout_view, name="logout"),
    path('account/signup', account.views.signup_view, name="signup"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
