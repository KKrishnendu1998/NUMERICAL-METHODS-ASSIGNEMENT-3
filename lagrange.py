"""interpolation of data 
creator : Krishnendu Maji
"""
from scipy.interpolate import *
from numpy import *
import matplotlib.pyplot as plt
x=[0,1,2,3,4,5]
y=[1.0,2.0,1.0,0.5,4.0,8.0]  #taking the data 
pol=lagrange(x,y)                        #lagrange interpolation 
xp=linspace(0,5,1000)
plt.plot(xp,pol(xp),color='k',label='lagrange')              #plotting lagrangian interpolation 
plt.scatter(x,y,label='original')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.title('lagrange interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
