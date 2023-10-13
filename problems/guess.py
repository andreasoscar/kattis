import sys
import math
r = range(1,1000)
print("500",flush=True)
it = 0
for line in sys.stdin:
    line = line.rstrip()
    
    if(line == "correct"):
       sys.exit()
    elif(line == "lower"):
        if(r.stop-r.start==4):
            print(r.start+1,flush=True)
            sys.exit()
        elif(r.stop==1000):
            r = range(r.start,500)
            print("250",flush=True)
        else:
            if r.start == 1:
                r = range(1, math.ceil(r.stop/2))
                print(math.ceil(r.stop/2),flush=True)
            else:
                r = range(r.start, math.ceil((r.start+r.stop)/2))
                print(math.ceil((r.start+r.stop)/2),flush=True)
    elif(line == "higher"):
        if(r.stop-r.start==4):
            print(r.stop-1,flush=True)
            sys.exit()
        elif(r.stop/2 == 500):
            r = range(500, r.stop)
            print("750",flush=True)
        else:
            if r.start == 1:
                r = range(math.ceil(r.stop/2), r.stop)
                print(math.ceil(r.start/2+r.stop/2),flush=True)
            else:
                r = range(math.ceil((r.start+r.stop)/2), r.stop)
                print(math.ceil((r.start+r.stop)/2),flush=True)
    
