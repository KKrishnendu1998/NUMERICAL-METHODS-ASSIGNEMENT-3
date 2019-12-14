"""various integartion method 
creator : Krishnendu Maji """
from numpy import *
from scipy.integrate import *
def func(x):              #defining the function #
    return exp(x)
x=linspace(0,1,100)
y=func(x)
print("trapezoidal =",trapz(y,x))      #trapezoidal method#
print('simpson=',simps(y,x))           #simpson's method#
print('romberg=',romberg(func,0,1))    #romberg method #
print('fixed_quad=',fixed_quad(func,0,1,n=5))  #gaussian quadrature method #
