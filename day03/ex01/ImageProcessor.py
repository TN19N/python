import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageProcessor :
    
    def load(self, path) :
        try :
            arr = mpimg.imread(path)
            print(f'Loading image of dimensions {arr.shape[0]} x {arr.shape[0]}')
            return arr
        except Exception as error:
            print(f'Exception: {type(error).__name__} -- strerror: {error.strerror if hasattr(error, "strerror") is True else None}')
            return None
    
    def display(self, array) :
        try :
            plt.imshow(array)
            plt.show()
        except Exception as error:
            print(f'Exception: {type(error).__name__} -- strerror: {error.strerror if hasattr(error, "strerror") is True else None}')