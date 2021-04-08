
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup),
    path('login/', views.login_call),
    path('forgotpassword/', views.forgot),
    path('reset/', views.reset_password),
    path('home/', views.home),
    path('logout/', views.logout_call),
    path('seller/', include('seller.urls')),
    path('buyer/', include('buyer.urls'))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)