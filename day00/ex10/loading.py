from time import time, sleep 

def ft_progress(listy) :
    startTime = time()
    estX = None
    for i in listy :
        if i != listy.start and estX == None:
            estX = (time() - startTime)
        lodingPercentage = int((i + 1) / len(listy) * 100)
        lodingBar = ('='*int(lodingPercentage*20/100) + '>')
        est = (len(listy) - (i + 1)) * estX if estX else 0.01
        print(f'ETA: {est:.02f}s [ {lodingPercentage}%] [{lodingBar:21}] {i + 1}/{len(listy)} | elapsed time {time() - startTime:.2f}s', end='\r')
        yield i 

if __name__ == '__main__' :
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)