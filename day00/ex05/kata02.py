kata = (2019, 9, 25, 3, 30)

if __name__ == '__main__' :
    print (f'{str(kata[2]).zfill(2)}/{str(kata[1]).zfill(2)}/{kata[0]} {str(kata[3]).zfill(2)}:{str(kata[4]).zfill(2)}')