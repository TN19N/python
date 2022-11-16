from copy import deepcopy

class CsvReader():

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try :
            self.file = open(self.filename, 'r')
            self.content = self.file.readlines()
            self.content = [[word.strip() for word in line.split(self.sep)] for line in self.content]
            standard = len(self.content[0])
            if all(len(line) == standard for line in self.content) is False :
                return None
            return self
        except :
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        try : 
            self.file.close()
        except :
            pass

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom. 
        Return:
            nested list (list(list, list, ...)) representing the data.
        """
        return deepcopy(self.content[self.skip_top:len(self.content) - self.skip_bottom:])

    def getheader(self):
        """ Retrieves the header from csv file. 
        Returns:
                list: representing the data (when self.header is True).
                None: (when self.header is False).
        """

        if self.header is False :
            return None
        return deepcopy(self.content[0:1:][0])