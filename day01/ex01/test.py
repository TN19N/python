from game import Stark

if __name__ == '__main__':
    
    arya = Stark("Arya")
    
    print(arya.__dict__)
    
    arya.print_house_words()
    
    print(arya.is_alive)
    
    arya.die()
    
    print(arya.is_alive) 
