import numpy as np

class NumpyCreator :
    
    def from_list(self, lst, dtype = float) :
        try :
            if type(lst) is not list :
                return None
            return np.array(lst, dtype = dtype)
        except :
            return None

    def from_tuple(self, tpl, dtype = float) :
        try :
            if type(tpl) is not tuple :
                return None
            return np.array(tpl, dtype = dtype)
        except :
            return None
    
    def from_iterable(self, itr, dtype = float) :
        try :
            return np.fromiter(itr, dtype = dtype)
        except :
            return None
    
    def from_shape(self, shape, value, dtype = float) :
        try :
            return np.full(shape, value, dtype = dtype)
        except :
            return None
    
    def random(self, shape) :
        try :
            return np.random.rand(shape[0], shape[1])
        except :
            return None
    
    def identity(self, n, dtype = float) :
        try :
            return np.identity(n, dtype = dtype)
        except :
            None