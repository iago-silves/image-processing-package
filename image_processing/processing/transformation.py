from skimage.transform import resize

def resize_image(image, proportion):
    assert 0 < proportion <= 1, "A proporção deve estar no intervalo (0, 1]"
    
    height = round(image.shape[0] * proportion)
    width = round(image.shape[1] * proportion)
    
    # Redimensiona a imagem com anti-aliasing e preservação dos valores originais
    image_resized = resize(image, (height, width), anti_aliasing=True, preserve_range=True)
    
    return image_resized
