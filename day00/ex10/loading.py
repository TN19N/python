from time import time, sleep 

def ft_progress(listy) :
    startTime = time()
    currTime = 0
    estX = 0.01
    for i in listy :
        lodingPercentage = int((i + 1) / len(listy) * 100)
        lodingBar = ('='*int(lodingPercentage*20/100) + '>')
        if abs(estX - ((time() - startTime) - currTime)) > 0.01:
            estX = (time() - startTime) - currTime
        est = (len(listy) - (i + 1)) * estX
        currTime = time() - startTime
        print(f'ETA: {est:.02f}s [ {lodingPercentage}%] [{lodingBar:21}] {i + 1}/{len(listy)} | elapsed time {currTime:.2f}s', end='\r')
        yield i 