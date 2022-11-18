import numpy as np

class ColorFilter :
    
    def invert(self, array): 
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        try :
            return 1 - array[:,:,:3]
        except :
            return None
    
    def to_blue(self, array): 
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        try :
            cp = array.copy()
            cp[:,:,0:2:] = 0.0
            return cp
        except :
            return None
    
    def to_green(self, array): 
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        try :
            cp = array.copy()
            cp[:,:,0:3:2] = 0.0
            return (cp)
        except :
            return None
    
    def to_red(self, array): 
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        try :
            cp = array.copy()
            cp[:,:,1:3:] = 0.0
            return (cp)
        except :
            return None
    
    def to_celluloid(self, array): 
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args: 
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        try :
            cp = array.copy()
            return cp
        except :
            return None
    
    def to_grayscale(self, array, filter, **kwargs): 
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in ['m','mean','w','weight']
            weights: [kwargs] list of 3 floats where the sum equals to 1,
                    corresponding to the weights of each RBG channels.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        try :
            if filter in ['m', 'mean'] :
                return 0.07 * array[:,:,2] + 0.72 * array[:,:,1] + 0.21 * array[:,:,0]
            if filter in ['w', 'weight'] and sum(kwargs['weights']) == 1.0 :
                return kwargs['weights'][0] * array[:,:,2] + kwargs['weights'][1] * array[:,:,1] + kwargs['weights'][2] * array[:,:,0]
            return None
        except :
            return None