import matplotlib.pyplot as plt
import seaborn

class MyPlotLib :
    
    def histogram(self, data, features) :
        data.hist(features)
    
    def density(self, data, features) :
        data[features].plot(kind='density')
    
    def pair_plot(self, data, features) :
        seaborn.pairplot(data[features], diag_kind="hist")
    
    def box_plot(self, data, features) :
        data[features].plot(kind='box')