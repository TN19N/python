from MyPlotLib import MyPlotLib

class Komparator :
    
    def __init__(self, data) :
        self.data = data
        self.lib = MyPlotLib()
        
    def compare_box_plots(self, categorical_var, numerical_var) :
        for categori in categorical_var :
            self.lib.box_plot(self.data[self.data.Sex == 'M'], [categori])
            self.lib.box_plot(self.data[self.data.Sex == 'F'], [categori])
            
    def density(self, categorical_var, numerical_var) :
        for categori in categorical_var :
            self.lib.density(self.data[self.data.Sex == 'M'], [categori])
            self.lib.density(self.data[self.data.Sex == 'F'], [categori])
            
    def compare_histograms(self, categorical_var, numerical_var) :
        for categori in categorical_var :
            self.lib.histogram(self.data[self.data.Sex == 'M'], [categori])
            self.lib.histogram(self.data[self.data.Sex == 'F'], [categori])