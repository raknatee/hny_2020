# plese use: python -u hny.py
#   for run this program
import sys
import time
from termcolor import colored
my_print=sys.stdout.write
colors=['red','green','yellow','blue','magenta','cyan','white']
str_show="happy new year 2020".upper()
pic='''

     .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. |
    | |    _____     | || |     ____     | || |    _____     | || |     ____     | |
    | |   / ___ `.   | || |   .'    '.   | || |   / ___ `.   | || |   .'    '.   | |
    | |  |_/___) |   | || |  |  .--.  |  | || |  |_/___) |   | || |  |  .--.  |  | |
    | |   .'____.'   | || |  | |    | |  | || |   .'____.'   | || |  | |    | |  | |
    | |  / /____     | || |  |  `--'  |  | || |  / /____     | || |  |  `--'  |  | |
    | |  |_______|   | || |   '.____.'   | || |  |_______|   | || |   '.____.'   | |
    | |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------' 

'''
# colors=['grey','red','green','yellow','blue','magenta','cyan','white']
print()
def getColor(index:int)->str:
    return colors[index%len(colors)]
def print_timer(i:int,timeout:int)->None:
    i='\t'+str(i)
    my_print(colored(i,getColor(int(i))))
    time.sleep(timeout)
    my_print('\b'*int(len(i)))
    my_print(' '*int(len(i)))
    my_print('\b'*int(len(i)))
#print countdown
for i in range(10,0,-1):
    print_timer(i,1)

for i in range(len(str_show)):
    if(i==0):
        print(colored('\t'+str_show[i],getColor(int(i))),end="")
    else:
        print(colored(str_show[i],getColor(int(i))),end="")
    time.sleep(0.25)
for i in range(len(pic)):
    print(colored(pic[i],'white'),end="")
    time.sleep(0.00025)

