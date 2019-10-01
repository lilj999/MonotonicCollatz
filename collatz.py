# Author: Longjiang Li, 
#           longjianglee@gmail.com
# Code function: used to generate a monotonic increasing Collatz series of any limited length $n$ with the same step size 1.
#   The Collatz conjecture is a conjecture in mathematics that concerns a series for any positive integer n.  If it's even, 
#   divide it by two, and if it's odd, multiply it by three and add one.  The Collatz conjecture  asserts that this series 
#   always falls into 4->2->1 cycles.
#    
import numpy as np
import matplotlib.pyplot as plt

####
#  
#  Function: calculate a Collatz series starting with n
#            variable re will store the series as a list if record is True
#
####
def S(n, record=False):
    re=[n]
    MAXCOUNT=99999
    i=MAXCOUNT
    c2=0
    c3=0
    maxn=0
    n0=n
    while n>1 and i>-1:
        
        if n % 2 !=0:
            n= n* 3+1 
            c3=c3+1
        #while n % 2==0:
        else:
            n= n//2
            c2=c2+1
        
        if maxn<n:
            maxn=n
   
        if record:
            re.append(n)
        i=i-1
    return n0,MAXCOUNT-i,re,c2,c3,maxn, maxn*1.0//n0     

###########
#   The Function of Monotonic(n, K1, K2, K3) is to calculate monotonic increasing series of any limited length $n$ with the same step size 1.
#   Explainations:         
#   1) All number like "K * 2^(n+1)-1" can generate a monotonic increasing series of length n;
#   2) Given K, the serie starting with  K*2^(n+1)-1 ending with 6 * K * 3^(n-1) -1;
#   3) K=1 is corresponding to the minimal x_1 that satisfies the monotonic constraints with the step size 1;
#   4) The function compares three series with (K1,K2,K3), and draw them side by side in a window.
#      
#   Example:  
#      Monotonic(10,3,4,5) compares three series starting with (3 * 2^11-1, 4* 2^11-1, 5* 2^11-1).
#      Monotonic(199,4,5,6) compares three series starting with (4 * 2^200-1, 5* 2^200-1, 6* 2^200-1).
#             
############
def Monotonic(n, K1=0, K2=1, K3=2):
    x1=K1 * pow(2,n+1)-1
    y1=4*K1*pow(3,n-1)-1
    flag,cn,re1,c2,c3,mn, mnb=S(x1,True)
    print('K1=',K1,' Y1=',y1,re1)
    x1=K2 * pow(2,n+1)-1
    y2=4*K2*pow(3,n-1)-1
    flag,cn,re2,c2,c3,mn, mnb=S(x1,True)
    print('K2=',K2,' Y2=',y2,re2)
    x1=K3 * pow(2,n+1)-1
    y3=4*K3*pow(3,n-1)-1
    flag,cn,re3,c2,c3,mn, mnb=S(x1,True)
    print('K3=',K3,' Y3=',y3,re3)

    label1= 'x_1={} * 2^({}+1)-1'.format(K1, n)
    label2= 'x_1={} * 2^({}+1)-1'.format(K2, n)
    label3= 'x_1={} * 2^({}+1)-1'.format(K3, n)

    minx= min(len(re1),len(re2),len(re3))
    x=range(minx)
    #y1= re1[x]
    plt.figure(num=3,figsize=(8,5))
    plt.plot(x,re1[:minx],color='black',linestyle='solid', label=label1)
    plt.plot(x,re2[:minx],color='black',linewidth=1,linestyle='--',label=label2)
    plt.plot(x,re3[:minx],color='black',linestyle='dotted',label=label3)
    plt.legend()
    plt.xlabel('Step of operations')
    plt.ylabel('The Collatz orbits')
    plt.show()

# examples
#Monotonic(10,1,2,3)
Monotonic(199,3,4,5)
