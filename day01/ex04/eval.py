class Evaluator :

    def __init__(self) -> None:
        self.A = 10

    def zip_evaluate(, coefs, words) :
        if type(coefs) != list or type(words) != list or len(coefs) != len(words) \
            or not all(type(c) == float and type(w) == str for (c, w) in zip(coefs, words)) :
            return -1
        res = 0
        for (c, w) in zip(coefs, words) :
            res += c * len(w)
        return res

    def enumerate_evaluate(coefs, words) :
        if type(coefs) != list or type(words) != list or len(coefs) != len(words) \
            or not all(type(c) == float and type(w) == str for (c, w) in zip(coefs, words)) :
            return -1
        res = 0
        for (i, w) in enumerate(words) :
            res += coefs[i] * len(w)
        return res