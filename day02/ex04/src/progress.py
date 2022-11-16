from time import time 

def ft_progress(listy) :
    startTime = time()
    for i in listy :
        lodingPercentage = int((i + 1) / len(listy) * 100)
        lodingBar = ('='*int(lodingPercentage*20/100) + '>')
        est = (len(listy) - (i + 1)) * 0.01
        print(f'ETA: {est:.2f}s [ {lodingPercentage}%] [{lodingBar:21}] {i + 1}/{len(listy)} | elapsed time {time() - startTime:.2f}s', end='\r')
        yield i 