
from rest_framework.response import Response
from .models import UploadedImage
from .serializers import UploadedImageSerializer

from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage

from myapp.models import UploadedImage

# User = get_user_model()#

# @login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save(commit=False)
            image_instance.user = request.user  # Assign authenticated user to 'user' field
            image_instance.save()
            return redirect('/upload')  # Redirect to image list view or another URL
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})



def print_image_names(request):
    uploaded_images = UploadedImage.objects.all()
    for image in uploaded_images:
        print(image.image.name)  # Print image names in console
    return render(request, 'template_name.html', {'uploaded_images': uploaded_images})