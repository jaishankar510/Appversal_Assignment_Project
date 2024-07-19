
from django.urls import path
from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    # path('images/', views.UserUploadedImageList.as_view(), name='user_uploaded_images'),
    path('print_image_names/', views.print_image_names, name='print_image_names'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)