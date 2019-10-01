# MonotonicCollatz
Code  is used to generate a monotonic increasing Collatz series of any length $n$ with the same step size 1.

The further information please refers to the paper:
  https://arxiv.org/abs/1909.13218

The Function of Monotonic(n, K1, K2, K3) is to calculate monotonic increasing series of any limited length $n$ with the same step size 1.
   Explainations:         
   1) All number like "K * 2^(n+1)-1" can generate a monotonic increasing series of length n;
   2) Given K, the serie starting with  K*2^(n+1)-1 ending with 4 * K * 3^(n-1) -1;
   3) K=0 is corresponding to the minimal x_1 that satisfies the monotonic constraints with the step size 1;
   4) The function compares three series with (K1,K2,K3), and draw them side by side in a window.
      
   Example:  
      Monotonic(10,  3,4,5) compares three series starting with (3 * 2^11-1, 4* 2^11-1, 5* 2^11-1).
      Monotonic(199, 4,5,6) compares three series starting with (4 * 2^200-1, 5* 2^200-1, 6* 2^200-1).
      
  The following figure shows the results for Monotonic(7, 1,2,3)    
  

  
 ![image](https://github.com/lilj999/MonotonicCollatz/blob/master/sim_incr.jpg)
