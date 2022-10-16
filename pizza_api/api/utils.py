# from PIL import Image
from io import BytesIO  #basic input/output operation
from PIL import Image,ImageOps #Imported to compress images
from django.core.files import File #to store files

def optimize_image(image):
    image_to_optimize = Image.open(image)
    base_width = 500
    #resize image
    width_ratio = (base_width/float(image_to_optimize.size[0]))
    height_size = int((float(image_to_optimize.size[1])*float(width_ratio)))
    image_to_optimize = image_to_optimize.resize((base_width,height_size), Image.Resampling.LANCZOS)
    # Convert Image to RGB color mode
    image_to_optimize = image_to_optimize.convert('RGB')
    # auto_rotate image according to EXIF data
    image_to_optimize = ImageOps.exif_transpose(image_to_optimize)
    # save image to BytesIO object
    image_to_optimize_io = BytesIO() 
    # save image to BytesIO object
    image_to_optimize.save(image_to_optimize_io, 'JPEG', quality=70) 
    # create a django-friendly Files object
    new_image = File(image_to_optimize_io, name=image.name)
    # Change to new image
    return new_image