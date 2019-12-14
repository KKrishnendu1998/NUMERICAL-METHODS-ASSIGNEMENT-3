"""interpolation of data 
creator : Krishnendu Maji
"""
from scipy.interpolate import *
from numpy import *
import matplotlib.pyplot as plt
x=[0,1,2,3,4,5]
y=[1.0,2.0,1.0,0.5,4.0,8.0]  #taking the data 
s=InterpolatedUnivariateSpline(x,y,k=1)  #linear spline
xp=linspace(0,5,1000)
plt.plot(xp,s(xp),color='green',label='linear spline')  #plotting linear spline
plt.scatter(x,y,label='original')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.title('linear interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
