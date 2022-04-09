from PIL import Image

def image_intake(img):
    img = Image.open(img)
    img = img.convert('L')
    return img