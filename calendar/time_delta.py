import sys
import datetime

def time_delta(t1, t2):
    format = "%a %d %b %Y %X %z"
    #a = datetime.datetime.strptime(t1, "%a %d %b %Y %X %z")
    #b = datetime.datetime.strptime(t2, "%a %d %b %Y %X %z")
    return abs(int((datetime.datetime.strptime(t1, format) - datetime.datetime.strptime(t2, format)).total_seconds()))
    
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
