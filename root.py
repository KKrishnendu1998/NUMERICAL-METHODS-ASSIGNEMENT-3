"""Finding the root of an equation 
creator : Krishnendu Maji """
from scipy.optimize import *
from numpy import *
def fun(x):                  #defining the function#
    return sin(cos(exp(x)))
def fder(x):                 #defining the derivative of the function #
    return -exp(x)*sin(exp(x))*cos(cos(exp(x)))
r1=bisect(fun,-1,1,rtol=0.0000000001,xtol=0.00000000001)   #bisection method using (-1,1) as starting bracket  #
r2=newton(fun,-1,fder)                                     #Newton-Raphson method with -1 as initial guess #
r3=newton(fun,-0.1,fder)                                   #Newton-Raphson method with -0.1 as initial guess #
r4=newton(fun,-0.1)                                        #Secand method (without specifying the derivative )#
print('root of the equation using bisection method with (-1,1) as initial bracket =', r1)
print('root of the equation using Newton-Rapshson method with -1 as initial guess =',r2)
print('root of the equation using Newton-Rapshson method with -0.1 as initial guess =',r3)
print('root of the equation using secant method ie, without defining the derivative in the command for newton-Raphson method =',r4)
# If use we bisection method using (-1,1) as starting bracket the root is 0.4515827052819077. If we use Newton-Raphson method with -1 as initial guess the value of the root is 9.179198883610521. Then I again use the Newton-Raphson method with -0.1 as my initial guess .This time I got the value of the root as 0.4515827052894549 which is quite similar with root I got using besection method. So,the answer changed when I use -0.1 as myb initial guess instead of -1.The reason can be explained as follow. If I plot the graph of the integrand  function we see that  the function is highly oscillating after the value x=2 or something.So,it has a root near 0.4515 ,a root near 1.55,a root near 2.09 .after this the the function becomes highly oscillating and we get so many roots .This is because of the exponential factor.Now we also plot the derivative of the function we see that at x=-1 the value of the  derivative of the  function quite small.So, as in Newton-Raphson method when we calculate the next value of x from our initial guess the derivative of the function occurs at the denominator.So, as the derivative is small at x=-1 we get the root 9.179198883610521,which is large.On the contrary , the derivative of the function at x=-0.1 is quite large .So, we get the nearest root of the value x=-0.1 which is  0.4515827052894549.#	

