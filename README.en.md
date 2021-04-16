# Python-for-Numworks
Python scripts for the Calculator <a href="https://www.numworks.com/">Numworks</a>

## How to install mathsup and physicsup
1. Installation
**ONLY WITH CHROME**
First of all, go to my workshop at numworks <a href="https://workshop.numworks.com/python/mino-1289/">here</a>.  
Plug your calculator in your computer and press the `Send to the Calculator` button.  

2. Using the commands  
Now that you have installed mathsup and/or physicsup, you will be able to use them.  
Unplug your calculator, and open the python app, then, make sure that only mathsup.py and physicsup.py are imported to the console.
To check that, on each script, go in the `...` that you see next to the name of the program, and press `OK` or `EXE`
finally, go down and check the auto-importation in the console.  
Go to the console, press `var`, a list of commands will appear, choose one of them, press `OK` or `EXE`.  
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

>>> dioph(a,b) # return the couple (u,v) so a*u+b*v = 1  

>>> dioph(a,b,c) # return the couple (u,v) so a*u+b*v = c 

>>> dioph(a,b,c,1) # return the couple list (u,v) so a*u+b*v = 1

>>> dioph(a,b,?c,?1) # In general : return always a couple (u,v) so a*u+b*v = c
                     # If c is not defined, c = 1
                     # If 1 is not defined, 1 = 0, thus return a couple (u,v)
                     # Else, return all couples list.

>>> disc(a,b,c) # return b²-4*a*c  

>>> dive(a,n) # return the couple of the euclide's division of a by n : (q,r) -> a = n*q+r

>>> divint(n) # return a list of all the integer that divide n

>>> fact(n) # return n!

>>> factor(n) # return a list of all the prime factor of n

>>> gdiv(n) # return the greatest common divisor of n (different from n)

>>> gprdiv(n) # return the greatest prime common divider of n

>>> int_bin(n) # return n in binary

>>> iscong(a,b,n) # return bool if a ≡ b [n]

>>> nprime(n) # return the list of all the prime number between 0 and n

>>> pi(n) # return an approximation of pi, more accurate for big n

>>> permut(n) # return all the permutation of n element i.e. n!

>>> pgcd(a,b) # return the greatest common divisor of a and b

>>> ppcm(a,b) # return the smallest commun muliplier of a and b

>>> prime(n) # return bool if n is a prime integer

>>> q(a,n) # return the integer quotient of the euclide's division of a by n.

>>> r(a,n) # return the rest of the euclide's division of a by n, only positive value.

>>> sdiv(n) # return the smallest divisor of n (different from 1)

>>> sprdiv(n) # return the smallest prime divisor of n

>>> tp(x,y,z) # return bool if x,y,z is a pythagorician triplet.


# physicsup :
>>> pvnrt(p,v,n,t) # return the value that you want, pass all the parameter you have and the one you want to know the value, 
                   # put a "" in the function, it will be calculated. 

>>> rho(m,V,p) # same operating system here is p = m/V, you can use it on every equation like this. 
```

#### Questions ?
Feel free to dm me on Discord : `Mino#1289`
Or create an issue and explain what is your problem with :)
