#Shehab Eldin Tarek 
#shehababaas123@gmail.com
# Master_micro.
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
s=[]
s1=[]
s2=[]
def objective(x):
    x1=x[0]
    y=x[1]
    funcv=((x1**2) - (10*x1) + (y**2) - (14*y) + 28) 
    s2.append(funcv)
    return (funcv)  
def constraint_1(x):
  x1=x[0]
  y=x[1]
  con_1=(x1+y-8)
  s1.append(con_1)
  return (con_1)
def constraint_2(x,con_2):
  x1=x[0]
  y=x[1]
  con_2=np.nan
  s2.append(con_2)
  return (con_2)  
x_int=float(input('x_intialize:'))
y_int=float(input('y_intialize:'))
x0=np.array([x_int,y_int])
con1=({'type':'eq','fun':constraint_1})
con2=({'type':'ineq','fun':constraint_2})
cons=[con1,con2]
sol=minimize(objective,x0,method='SLSQP',constraints=con1,options = {"disp": True})
xop=sol.x
vop=sol.fun
print(vop)
plt.xlabel('Cost Function')
plt.ylabel('Iteration')
plt.title('Iteration Vs Cost Function.')
plt.plot(range(1,len(s2)+1),s2);
