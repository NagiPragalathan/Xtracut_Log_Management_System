"""Finalty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from base.Routes.ApiViews import *
from base.Routes.views import *


from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Finalty import settings
from django.contrib.sitemaps.views import sitemap
from base.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}


ApiviewsUrl = [
    path('api/create/', api_create_log, name='api_create_log'),
    path('api/read/<uuid:log_id>/', api_read_log, name='api_read_log'),
    path('api/update/<uuid:log_id>/', api_update_log, name='api_update_log'),
    path('api/delete/<uuid:log_id>/', api_delete_log, name='api_delete_log'),
]

ViewsUrl = [
    path('test/create/', create_log, name='create_log'),
    path('test/list/', log_list, name='log_list'),
    path('test/update/<uuid:log_id>/', update_log, name='update_log'),
    path('test/delete/<uuid:log_id>/', delete_log, name='delete_log'),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    # Seo Config...
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt),
]

urlpatterns+=ApiviewsUrl
urlpatterns+=ViewsUrl

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
