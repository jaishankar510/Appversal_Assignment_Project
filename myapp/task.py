
from celery import shared_task
from PIL import Image

@shared_task
def process_image(image_id):
    try:
        image_obj = UploadedImage.objects.get(id=image_id)
        img = Image.open(image_obj.image.path)
        img.thumbnail((300, 300))
        img.save(image_obj.image.path)
    except UploadedImage.DoesNotExist:
        pass 
