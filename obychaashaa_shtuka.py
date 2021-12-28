import sys,time


time.sleep(1)
for n,v in sys.modules.items():
    print(n,v,sep=": ")
import main