import sys, os
sys.path.append(os.path.abspath('../ex00'))

from FileLoader import FileLoader
from Komparator import Komparator

if __name__ == '__main__' :
    
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    
    kompar = Komparator(data)
    
    kompar.compare_box_plots()