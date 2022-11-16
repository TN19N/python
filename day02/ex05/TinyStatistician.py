import math 

class TinyStatistician:
    
    def mean(self, x) :
        try :
            if len(x) == 0 is True :
                return None
        except :
            return None
        else :
            return sum(x) / len(x)

    def median(self, x) : 
        try :
            if len(x) == 0 is True :
                return None
        except :
            return None
        else :
            return (x[int(len(x) / 2)] + x[~int(len(x) / 2)]) / 2

    def quartiles(self, x) :
        try :
            if len(x) == 0 is True :
                return None
        except :
            return None
        else :
            Q1 = (len(x) + 1) / 4
            Q2 = Q1 * 2
            Q3 = Q1 * 3
            return [x[0:int(Q1)],x[int(Q1):int(Q2)],x[int(Q2):int(Q3)],x[int(Q3):]]

    def var(self, x) :
        try :
            if len(x) == 0 is True :
                return None
        except :
            return None
        else :
            sum = 0
            mean = self.mean(x)
            for number in x :
                sum += math.pow(number - mean, 2)
            return sum / len(x)

    def std(self, x) :
        try :
            if len(x) == 0 is True :
                return None
        except :
            return None
        else :
            return math.sqrt(self.var(x))