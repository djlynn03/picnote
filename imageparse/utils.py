from PIL import Image
import pillow_heif

def image_intake(img):
    
    if img.name.endswith('.heif') or img.name.endswith('.heic') or img.name.endswith('.HEIF') or img.name.endswith('.HEIC'):
        img = pillow_heif.open(img)
        img = Image.frombytes(img.mode, img.size, img.data, "raw")
        return img.convert('RGB'), img.convert('L')
    
    img = Image.open(img)
    return img.convert('RGB'), img.convert('L')
