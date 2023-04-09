#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:
n=5

output:
*
* * 
* * * 
* * * * 
* * * * *

Hints:


Solution:
num=10
def show_pattern(num):
    for i in range(num):
        for j in range(i+1):
            print("*",end=" ")
        print()
show_pattern(num)

#--------------------------------------------------------------------------------#



#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
        *
      * * 
    * * * 
  * * * * 
* * * * *

Hints:


Solution:
num=10

def show_pattern(num):
    for i in range(num):
        for j in range(num-i):
            print(" ",end=" ")
        for k in range(i+1):
            print("*",end=" ")
        print()
        
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
* * * * * 
* * * *
* * * 
* * 
*

Hints:


Solution:
num=10

def show_pattern(num):
    for i in range(num):
        for j in range(num-i):
            print("*",end=" ")
        print()

show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
* * * * * 
  * * * *
    * * * 
      * * 
        *


Hints:


Solution:
num=10

def show_pattern(num):
    for i in range(num):
        for j in range(0,i):
            print(" ",end=" ")
        for j in range(num-i):
            print("*",end=" ")
        print()

show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
*                   *
* *		          * *
* * *           * * *
* * * *       * * * *
* * * * *   * * * * *
* * * * * * * * * * *

Hints:


Solution:
num=5

def show_pattern(num):
    for i in range(num):
        for j in range(i+1):
            print("*",end=" ")
        for j in range(num-i):
            print(" ",end=" ")
        for j in range(num-i):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
    print("* "*((num*2)+1))

show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
* * * * * 
* * * *
* * * 
* * 
*
*
* * 
* * * 
* * * * 
* * * * *

Hints:


Solution:
num=5

def show_pattern(num):
    for i in range(num):
        for j in range(num-i):
            print("*",end=" ")
        print()
    for i in range(num):
        for j in range(i+1):
            print("*",end=" ")
        print()

show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
* * * * * * * * * * *
* * * * *   * * * * *
* * * *       * * * * 
* * *           * * *
* *               * *
*                   *

Hints:


Solution:
def show_pattern(num):
    print("* "*((num*2)+1))
    for i in range(num):
        for j in range(num-i):
            print("*",end=" ")
        for j in range(i):
            print(" ",end=" ")
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(num-i):
            print("*",end=" ")
        print()
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
* * * * * 
  * * * *
    * * * 
      * * 
        *
		*
      * * 
    * * * 
  * * * * 
* * * * *


Hints:


Solution:
num=5

def show_pattern(num):
    for i in range(num):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(num-i):
            print("*",end=" ")
        print()
    for i in range(num):
        for j in range(num-i):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
* * * * * * * * * * 
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *		        * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *


Hints:


Solution:
num=5
def show_pattern(num):
    #upper part
    for i in range(num):
        for j in range(num-i):
            print("*",end=" ")
        for j in range(i+i):
            print(" ",end=" ")
        for j in range(num-i):
            print("*",end=" ")
        print()
    
    #lower part
    for i in range(num):
        for j in range(i+1):
            print("*",end=" ")
        for j in range((num-1)-i):
            print(" ",end=" ")
        for j in range((num-1)-i):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print() 
   
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
    *
   * *
  * * *
 * * * *
* * * * *

Hints:


Solution:
num=5
def show_pattern(num):
    for i in range(num):
        for j in range((num-1)-i):
            print(" ",end="")
        for j in range(i+1):
            print("*",end=" ")
        print()  
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
* * * * * 
 * * * *
  * * *
   * *
    *

Hints:


Solution:
num=5
def show_pattern(num):
    for i in range(num):
        for j in range(i):
            print(" ",end="")
        for j in range(num-i):
            print("*",end=" ")
        print()
     
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
* * * * * 
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *

Hints:


Solution:
num=5
def show_pattern(num):
    #upper part
    for i in range(num):
        for j in range(i):
            print(" ",end="")
        for j in range(num-i):
            print("*",end=" ")
        print()
    
    #lower part
    for i in range(num):
        for j in range((num-1)-i):
            print(" ",end="")
        for j in range(i+1):
            print("*",end=" ")
        print()
show_pattern(num)
#--------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
* * * * * * * * * * * * * * * 
 * * * *   * * * *   * * * * 
  * * *     * * *     * * * 
   * *       * *       * * 
    *         *         * 
 

Hints:


Solution:
num=5
def show_pattern(num):
    for i in range(num):
        for sp in range(i):
            print(" ",end="")
        for s in range(num-i):
            print("*",end=" ")

        for sp in range(i):
            print(" ",end=" ")
        for s in range(num-i):
            print("*",end=" ")

        
        for sp in range(i):
            print(" ",end=" ")
        for s in range(num-i):
            print("*",end=" ")
        
        print()
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
     *
    ***
   *****
  *******
 *********

Hints:


Solution:
num=5
def show_pattern(num):
    k=1
    for i in range(num):
        for j in range(num-i):
            print(" ",end="")
        for j in range(0,k):
            print("*",end="")
        print()
        k=k+2
   
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
    **
   ****
  ****** 
 ********
**********
Hints:


Solution:
num=5
def show_pattern(num):
    k=2
    for i in range(num):
        for j in range(num-i):
            print(" ",end="")
        for j in range(0,k):
            print("*",end="")
        print()
        k=k+2

     
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:
num=5

output:

* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
* * * * * * 
* *     * * * * 
* * *         * * * 
* * * *             * * 
* * * * *                 *   


Hints:


Solution:
num=5

def show_pattern(num):
    #upper part
    for i in range(num):
        for j in range(num-i):
            print("*",end=" ")
        for j in range(i+i):
            print(" ",end=" ")
        for j in range(num-i):
            print("*",end=" ")
        print()
    
    #lower part
    for i in range(num):
        for j in range(i+1):
            print("*",end=" ")
        for j in range(i+i):
            print(" ",end=" ")
        for j in range(num-i):
            print("*",end=" ")
        print() 
   
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
a
a a
a a a
a a a a
a a a a a   


Hints:


Solution:
num=5
def show_pattern(num):
    for i in range(num):
        for j in range(i+1):
            print("a",end=" ")
        print()
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
a
b b
c c c
d d d d
e e e e e

Hints:


Solution:
num=5
def show_pattern(num):
    for i in range(num):
        for j in range(i+1):
            print(chr(ord("a")+i),end=" ")
        print()
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
a
a b
a b c
a b c d
a b c d e


Hints:


Solution:
num=5
def show_pattern(num):
    for i in range(num):
        for j in range(i+1):
            print(chr(ord("a")+j),end=" ")
        print()
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
e e e e e
d d d d
c c c
b b
a

Hints:


Solution:
num=5
def show_pattern(num):
    for i in range(num):
        for j in range(num-i):
            print(chr((ord('a')+(num-1))-i),end=" ")
        print()

show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
e d c b a
e d c b
e d c
e d
e


Hints:


Solution:
num=5
def show_pattern(num):
    for i in range(num):
        for j in range(num-i):
            print(chr((ord('a')+(num-1))-j),end=" ")
        print()
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:
a b c d e
a b c d 
a b c 
a b 
a 


Hints:


Solution:
num=5
def show_pattern(num):
    for i in range(num):
        for j in range(num-i):
            print(chr((ord('a'))+j),end=" ")
        print()
show_pattern(num)

#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:


Hints:


Solution:


#--------------------------------------------------------------------------------#


#---------------------------------------------------------------------------------#
Question:
Printing follwing pattern.

Input:


output:


Hints:


Solution:


#--------------------------------------------------------------------------------#


