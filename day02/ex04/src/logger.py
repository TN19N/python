from time import time

logFile = open('machine.log', 'w')

def log(function) :
    def wrapper(*args, **kargs) :
        startTime = time()
        result = function(*args, **kargs)
        execTime = time() - startTime
        logFile.write(f'(cmaxime)Running: {function.__name__:18} [ exec-time = {execTime:.3f} {"ms" if execTime < 1 else "s"} ]\n')
        return result
    return wrapper