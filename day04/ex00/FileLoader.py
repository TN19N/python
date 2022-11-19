import pandas

class FileLoader :

    def load(self, path) :
        try :
            data = pandas.read_csv(path)
            print(f'Loading dataset of dimensions {" x ".join(str(num) for num in data.shape)}')
            return data
        except :
            return None
    
    def display(self, df, n) :
        try:
            print(type(n))
            if n >= 0 :
                print('----------+---------')    
                print(df.head(n))
            else :
                print('----------*---------')
                print(df.tail(-1 * n))
        except:
            print('None')