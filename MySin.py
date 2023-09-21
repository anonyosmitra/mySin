import numpy as np
import matplotlib.pyplot as plt
import math
from tabulate import tabulate

def factorial(i):
	if i==0 or i==0:
		return 1
	return i*factorial(i-1)

def isEven(i):
	if i%2==0:
		return 1
	else:
		return -1
		

def poly(x):
	rng=list(range(1,11,2))
	a=0
	for i in rng:
		a+=(math.pow(x,i)/factorial(i))*isEven(rng.index(i))
	return a



def mySin(x):
	si=1
	if x<0:
		x=-1*x
		si=-1
	while(x>=2*math.pi):
		x-=2*math.pi
	if(x<math.pi/2):
		return poly(x)*si
	elif(x<math.pi):
		return poly(math.pi-x)*si
	elif(x<math.pi*3/2):
		return -poly((x-math.pi))*si
	else:
		return poly(x-2*math.pi)*si

x=np.linspace(-4*math.pi,4*math.pi)
xaxis=[]
y1=[]
y2=[]
tab=[]
for i in x:
	xaxis.append(0)
	a1=math.sin(i)
	a2=mySin(i)
	y1.append(a1)
	y2.append(a2)
	tab.append([i,a1,a2,a1-a2])
plt.plot(np.array(x),np.array(xaxis),color="black")
plt.plot(np.array(x),np.array(y1),color="blue")
plt.plot(np.array(x),np.array(y2),color="red")
print(tabulate(tab,headers=["X","sin(x)","mySin(x)","sin(x)-mySin(x)"]))
plt.show()