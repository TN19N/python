class SpatioTemporalData :
    
    def __init__(self, data):
        self.data = data
    
    def when(self, location):
        return [*self.data.loc[self.data['City'] == location].Year.unique()]
    
    def where(self, date):
        return [*self.data.loc[self.data['Year'] == date].City.unique()]