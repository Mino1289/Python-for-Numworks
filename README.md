# Python-for-Numworks
Python scripts for the Calculator <a href="https://www.numworks.com/">Numworks</a>

## How to install mathsup and physicsup
1. Installation  
First of all, go to my workshop at numworks <a href="https://workshop.numworks.com/python/mino-1289/">here</a>.  
Plug your calculator in your computer and press the "Send to the Calculator" button.  

2. Using all the commands  
Now that you have installed mathsup and/or physicsup, you wille be able to use them.  
Unplug your calculator, and open the python app, then, make sure that only mathsup.py and physicsup.py are imported to the console.
If not, go in the `...` that you see next to the name of the program, and press `OK` or `EXE`, then go down and check the auto-importation in the console.  
Then go to the console, press `var`, a list of commands will appear, choose one of them, press `OK` or `EXE`.  
In the console, you called a function, now you have to pass all the require parameters splitted by a comma and then press `OK` or `EXE`.  

### All the functions :
```py
from mathsup import *
from physicsup import *
# mathsup :
>>> arran(n,k) # return the number of arrangement of k element among n  

>>> bin_int(n) # return an integer of the binary number n  

>>> combi(n,k) # return the number of element of k element among n  

>>> cong(a,n) # return (b, c), the closest int that a ≡ (b, c) [n] (b is positive and c not)  

>>> congi(a,n) # return the closest integer b so a ≡ b [n] (b can be negative)  

>>> dioph(a,b) # return value (u,v) so a*u+b*v = 1  

>>> dioph(a,b,c) # return value (u,v) so a*u+b*v = c  

>>> disc(a,b,c) # return b²-4*a*c  

>>> dive(a,n) # return the couple of the euclide's division of a by n : (q,r) -> a = n*q+r

>>> divint(n) # return a list of all the integer that divide n

>>> fact(n) # return n!

>>> factor(n) # return a list of all the prime factor of n

>>> int_bin(n) # return the binary integer of the value n

>>> iscong(a,b,n) # return bool if a ≡ b [n]

>>> log16(n) # return the logarithm 16-based of n

>>> permut(n) # return all the permutation of n element i.e. n!

>>> pgcd(a,b) # return the greatest commun divider of a and b

>>> pi(n) # return an approximation of pi, more accurate for big n

>>> ppcm(a,b) # return the smallest commun muliplier of a and b

>>> prime(n) # return bool if n is a prime integer

>>> q(a,n) # return the integer quotient of the euclide's division of a by n.

>>> r(a,n) # return the rest of the euclide's division of a by n, only positive value.

>>> rng(n) # return the value n ± 25%

>>> tp(x,y,z) # return bool if x,y,z is a pythagorician triplet.


# physicsup :
>>> pvnrt(p,v,n,t) # return the value that you want, pass all the parameter you have and the one you want to know the value, 
                   # put a "" in the function, it will be calculated. 

>>> rho(m,V,p) # same operating system here is p = m/V, you can use it on every equation like this. 
```

#### Some questions ?
Feel free to dm me on Discord : `Mino#1289`
