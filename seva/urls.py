"""seva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from convsort import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('uploadcv/<str:job>', views.Home, name='home'),
    path('upload/<str:job_id>', views.upload, name='upload'),
    path('', views.jobs, name='jobs'),
    path('admin_jobs/', views.admin_jobs, name='admin_jobs'),
    path('add_job/', views.add_job, name='add_job'),
    path('delete_job/<int:id>', views.delete_job,name='delete_job'),
    path('Admin/',views.admins,name='admins'),
    path('shortlist/',views.shortlist,name='shortlist'),
    path('select/<str:uid>/<str:jid>',views.select,name='select'),
    path('reject/<str:uid>/<str:jid>',views.reject,name='reject'),
    path('admin/', admin.site.urls),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),

    path('reg/',views.reg,name="reg"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
