from ex01.ImageProcessor import ImageProcessor 
from ex03.ColorFilter import ColorFilter 
from matplotlib import pyplot as plt


if __name__ == '__main__' :
    
    imp = ImageProcessor()
    arr = imp.load("./resources/elon_canaGAN.png")
    cf = ColorFilter()
    
    images = [(arr, 'originale')]
    images.append((cf.invert(arr), 'Inverted filter'))
    images.append((cf.to_green(arr), 'Green filter'))
    images.append((cf.to_red(arr), 'Red filter'))
    images.append((cf.to_blue(arr), 'Blue filter'))
    images.append((cf.to_celluloid(arr), 'Celluloid filter'))
    images.append((cf.to_grayscale(arr, 'm'), 'grayscale filter (mean)'))
    images.append((cf.to_grayscale(arr, 'weight', weights = [0.3, 0.4, 0.3]), 'grayscale filter (weight)'))

    print(arr.shape)

    for i, (image,title) in enumerate(images) :
        plt.subplot(3, 3, i+1)
        plt.imshow(image)
        plt.axis('off')
        plt.title(title)
    
    plt.show()