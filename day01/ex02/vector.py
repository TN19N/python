from copy import deepcopy

class Vector :
    def __init__(self, arg):
        if type(arg) == list and len(arg) and type(arg[0]) == list:
            self.values = arg
        elif type(arg) == int and arg >= 0:
            if arg == 0 : self.values = [[]]
            else : self.values = [[i] for i in range(0, arg)]
        elif type(arg) == tuple and len(arg) == 2 and arg[0] <= arg[1]:
            if arg[0] == arg[1] : self.values = [[]]
            else : self.values = [[i] for i in range(arg[0], arg[1])]
        else :
            raise NotImplementedError('not defined here')
        self.shape = (0 if len(self.values[0]) == 0 else len(self.values), len(self.values[0]))

    def __add__(self, other) :
        if type(other) != Vector or self.shape != other.shape :
            raise NotImplementedError('not defined here')
        tmp = deepcopy(self)
        for col in range(self.shape[0]) :
            for row in range(self.shape[1]) :
                tmp.values[col][row] += other.values[col][row]
        return tmp

    def __sub__(self, other) :
        if type(other) != Vector or self.shape != other.shape :
            raise NotImplementedError('not defined here')
        tmp = deepcopy(self)
        for col in range(self.shape[0]) :
            for row in range(self.shape[1]) :
                tmp.values[col][row] -= other.values[col][row]
        return tmp

    def __mul__(self, other) :
        if type(other) != Vector and type(other) != int and type(other) != float or type(other) == Vector and self.shape != other.shape:
            raise NotImplementedError('not defined here')
        tmp = deepcopy(self)
        for col in range(self.shape[0]) : 
            for row in range(self.shape[1]) :
                tmp.values[col][row] *= other if type(other) != Vector else other.values[col][row]
        return tmp

    def __rmul__(self, other) :
        return self.__mul__(other)

    def __truediv__(self, other) :
        if type(other) != Vector and type(other) != int and type(other) != float or type(other) == Vector and self.shape != other.shape:
            raise NotImplementedError('not defined here')
        tmp = deepcopy(self)
        for col in range(self.shape[0]) :
            for row in range(self.shape[1]) :
                if (other if type(other) != Vector else other.values[col][row]) == 0 : raise ZeroDivisionError('division by zero.')
                tmp.values[col][row] /= other if type(other) != Vector else other.values[col][row]
        return tmp

    def __rtruediv__(self, scalar) :
        raise NotImplementedError('Division of a scalar by a Vector is not defined here.')

    def T(self) :
        tmp = []
        for col in range(self.shape[0]) : 
            for row in range(self.shape[1]) :
                if row >= len(tmp): tmp.append([])
                tmp[row].append(self.values[col][row])
        return deepcopy(Vector(tmp))

    def dot(self, other) :
        if self.shape != other.shape :
            raise NotImplementedError('dot product between two vectors of different shape is not defined here.')
        res = 0
        for col in range(self.shape[0]) :
            for row in range(self.shape[1]) :
                res += self.values[col][row] * other.values[col][row]
        return res

    def __repr__(self) :
        return repr(self.values)

    def __str__(self):
        return str(self.values)
    