import matplotlib.pyplot as plt

# Plotagem simples de uma imagem
def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap="gray")
    plt.axis('off')
    plt.show()

# Plotagem de várias imagens lado a lado
def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))

    # Nomes automáticos para as imagens, mais "Result" ao final
    names = ['Image ({})'.format(i) for i in range(1, number_images)]
    if number_images > 1:
        names[-1] = "Result"  # Última imagem como "Result"
    else:
        names[0] = "Result"

    # Garante que 'axis' seja sempre iterável (mesmo com 1 imagem)
    if number_images == 1:
        axis = [axis]

    for ax, name, image in zip(axis, names, args):
        ax.set_title(name)
        ax.imshow(image, cmap='gray')
        ax.axis('off')

    fig.tight_layout()
    plt.show()

# Plotagem de histograma de uma imagem RGB
def plot_histogram(image):
    fig, axis = plt.subplots(nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True)
    color_list = ['red', 'green', 'blue']

    for index, (ax, color) in enumerate(zip(axis, color_list)):
        ax.set_title('{} Histogram'.format(color.title()))
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)

    fig.tight_layout()
    plt.show()
