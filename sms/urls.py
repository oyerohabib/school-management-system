from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import handler404, handler500
# from student_management_app.views import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_management_app.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = handler404
# handler500 = handler500