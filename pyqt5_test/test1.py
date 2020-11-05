import time
timeStamp = 0.73125*3600+9*3600
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M", timeArray)
print(otherStyleTime)