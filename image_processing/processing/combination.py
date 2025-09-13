import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Especifique 2 imagens com o mesmo formato"
    
    # Converte as imagens para escala de cinza
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    
    # Calcula o índice de similaridade estrutural
    score, difference_image = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similaridade das imagens:", score)
    
    # Normaliza a imagem de diferença para o intervalo [0, 1]
    normalized_difference_image = (difference_image - np.min(difference_image)) / (np.max(difference_image) - np.min(difference_image))
    
    return normalized_difference_image

def transfer_histogram(image1, image2):
    # Ajusta o histograma de image1 para se parecer com image2
    match_image = match_histograms(image1, image2, channel_axis=-1)
    return match_image
