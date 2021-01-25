#Shehab Eldin Tarek 
#shehababaas123@gmail.com
# Master_micro.
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
s=[]
s1=[]
s2=[]
def funv(x):
    x1=x[0]
    y=x[1]
    s.append(x1)
    s1.append(y)
    return ((x1**2) - (10*x1) + (y**2) - (14*y) + 28)  
def objective(x):
  x1=x[0]
  y=x[1]
  s.append(x1)
  s1.append(y)
  funcv=((x1**2) - (10*x1) + (y**2) - (14*y) + 28)  
  s2.append(funv(x))
  return funcv    
def constraint(x):
  x1=x[0]
  y=x[1]
  return (x1+y-8)
x_int=1
y_int=1
x0=np.array([x_int,y_int])
con1=({'type':'eq','fun':constraint})
sol=minimize(objective,x0,method='SLSQP',constraints=con1,options = {"disp": True})
xop=sol.x
vop=sol.fun
print(vop)
plt.plot(range(1,len(s2)+1),s2);
