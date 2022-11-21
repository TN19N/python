from MyPlotLib import MyPlotLib,plt
from FileLoader import FileLoader

if __name__ == '__main__' :
    
    lib = MyPlotLib()
    loader = FileLoader()
    
    data = loader.load('../data/athlete_events.csv')
    
    lib.histogram(data, ['Height', 'Weight'])
    
    lib.density(data, ['Height', 'Weight'])

    lib.pair_plot(data, ['Height', 'Weight'])

    lib.box_plot(data, ['Height', 'Weight'])

    plt.show()