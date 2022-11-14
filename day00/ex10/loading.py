from time import time, sleep 
from tqdm import tqdm

def ft_progress(listy) :
    startTime = time()
    for i in listy :
        lodingTime = time() - startTime
        lodingPercentage = int((i + 1) / len(listy) * 100)
        lodingBar = ('='*int(lodingPercentage*20/100) + '>')
        est = (len(listy) - (i + 1)) * 0.01
        print(f'ETA: {est:.2f}s [ {lodingPercentage}%] [{lodingBar:21}] {i + 1}/{len(listy)} | elapsed time {lodingTime:.2f}s', end='\r')
        yield i 

if __name__ == '__main__' :
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)