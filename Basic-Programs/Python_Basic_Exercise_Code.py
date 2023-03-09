#============================================================================================
>>Formae:
1.Question
2.Input
3.Output
4.Hints
#============================================================================================

#------------------------------------------------------------#
Question-1:
Hello, World! Program.

input:

output:

Solution:
print("Hello World...!")

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-2:
Program to Print an Integer Number and Add (Entered by the User).

input:
val=10
val2=20

output:
res=30

Solution:
print((int(input("enter no: "))) + (int(input("enter second no: "))))

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
Program to Multiply two Floating Point Numbers.

input:
val1=10
val2=20

output:
res=200

Solution:
print((eval(input("enter no: "))) * (eval(input("enter second no: "))))

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:
Program to Find ASCII Value of a Character.

input:
ch='A'
ch='Q'

output:
res=65
res=81

Hints:
-char to ASCII:
    ord()

-ASCII to char
    chr()

Solution:
ch=input("Enter charact: ")
print("ASCII Val:",ord(ch))

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:
Program to Compute Quotient and Remainder.

input:
Enter first number: 20
Enter second number: 3

output:
Remmainder:  2
Quentient:  6

Solution:
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
rem=num1%num2
quo=num1//num2
print("Remmainder: ",rem)
print("Quentient: ",quo)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Program to Swap Two Numbers.

input:
a=10 
b=20

output:
a=20
b=10

Solution:
#Type-1:----------------------------
num1,num2=10,20
print("Before swaping Numbers:")
print("num1:",num1,"\t","num2:",num2)
num3=num1
num1=num2
num2=num3
print("\nAfter swaping Numbers:")
print("num1:",num1,"\t","num2:",num2)


#Type-2----------------------------
num1,num2=30,40
print("Before swaping Numbers:")
print("num1:",num1,"\t","num2:",num2)
num3=num1+num2
num1=num3-num1
num2=num3-num1
print("\nAfter swaping Numbers:")
print("num1:",num1,"\t","num2:",num2)


#Type-3---------------------------
num1,num2=50,60
print("Before swaping Numbers:")
print("num1:",num1,"\t","num2:",num2)
num1=num1+num2;
num2=num1-num2;
num1=num1-num2;
print("\nAfter swaping Numbers:")
print("num1:",num1,"\t","num2:",num2)



#Type-4:------------------------
n1,n2=50,60
print("Before swaping Numbers:")
print("n1:",n1,"\t","n2:",n2)
n1=n1*n2;
n2=n1//n2;
n1=n1//n2;
print("n1=",n1 , "\t","n2=",n2,"\n")



#Type-5-------------------------
n1,n2=10,50
print("n1=",n1,"\t", "n2=",n2)
n1=n1^n2;
n2=n1^n2;
n1=n1^n2;
print("n1=",n1 ,"\t","n2=",n2)



#Type-6:-----------------------
n1,n2=20,50
print("n1=",n1,"\t", "n2=",n2)
n1,n2=n2,n1
print("n1=",n1,"\t", "n2=",n2)


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:
Program to Check Whether a Number is Even or Odd.

input:
num=10
num=13

output:
res=Even Number 
res=Odd Number 

Solution:
#Type-1--------------------------------------------
num=int(input("Enter Any number: "))
print("Enve Number" if(num%2==0) else "Odd Number")

#Type-2:-------------------------------------------
num=int(input("Enter Any number: "))
if (num%2==0):
    print("Even Number")
else:
    print("Odd Number")
    
#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:
Program to Check Whether a Character is Vowel or Consonant.

input:
ch='A'
ch='B'

output:
res=Vowel
res=Consonent

Solution:
ch=input("Pleasn enter character: ")
print("vowel" if(ch=='A' or ch=="E" or ch=="I" or ch=="O" or ch=="U" or ch=='a' or ch=="e" or ch=="i" or ch=="o" or ch=="u") else "Consonent")

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
Program to Find the Largest Number Among four Numbers.
input:
a,b,c,d=10,20,30,40
a,b,c,d=20,30,40,10

output:
res=a is max
res=c is max

Solution:
num1=int(input("enter first no: "))
num2=int(input("enter second no: "))
num3=int(input("enter third no: "))
num4=int(input("enter fouth no: "))
print("num1 Greater no" if(num1>num2 and num1>num3 and num1>num4) else "num2 Greater no" if(num2>num3 and num2>num4) else "num3 Greater no" if(num3>num4) else "num4 Greater no");

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-10:
Program to Check Leap Year.

input:
Please enter year: 2010
Please enter year: 2008

output:
res:Not leap year
res:Leap year

Solution:
Year=int(input("Please enter year: "))
print("Leap year" if((Year % 400 == 0) or (Year % 100 != 0) and  (Year % 4 == 0)) else "Not leap year")

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-11:
Program to Check Whether a Number is Positive or Negative or zero.

input:
val=10
val=-2
val=0

output:
res=Possitive
res=Negative
res=Zero

Solution:
number=int(input("Emter number: "))
print("Possitive number" if(number>0)  else "Negative" if (number<0) else "Zero")

#------------------------------------------------------------#


#------------------------------------------------------------#
Question12:
Program to Check Whether a Character is an Alphabet or not.

input:
val='A'
val=1
val=@

output:
res=Alphabet
res=Not Alphabet
res=Not Alphabet

Solution:
ch=input("Enter character: ")
print("Alphabet" if(ch.isalpha()) else "Not alphabet")

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-13:
Program to Calculate the Sum of Natural Numbers.

input:
number: 5

output:
1,2,3,4,5 || 1 + 2 + 3 + 4 + 5
res=15

Solution:
#Type-1----------------------------------------
number=int(input("Enter last interval val: "))
sum=0
for i in range(number+1):
    sum=sum+i
print(sum)

#Type-2---------------------------------------
num=int(input("Enter number: "))
add=0
while(num>0):
    add=add+num
    num=num-1
print("Add natural number: ",add)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-14:
Program to Find Factorial of a Number.

input:
val=5

output:
5,4,3,2,1 || 5 * 4 * 3 * 2 * 1
res=120

Solution:
#Type-1:-------------------------
num=int(input("Enter Number: "))
fact=1
while(num>0):
    fact=fact*num
    num=num-1
print("Factorial is: ",fact)

#Type-2:---------------------------------
number=int(input("Please enter number: "))
fact=1
for i in range(1,number+1):
    fact=fact*i
print("Factorial is: ",fact)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-15:
Program to Generate Multiplication Table.

input:
num=2

output:
2*1=2
2*2=4
- - -
- - - 
- - - 
2*10=20

Solution:
#Type-1:--------------------------------------------
print("Using for loop")
num=int(input("Enter No: "))
res=0;
for i in range(1,10+1,1):
    res=num*i;
    print(num,"*",i,"=",res)

    
#Type-2:------------------------------------------
print("\nWhile loop")
i=1
while(i<=10):
    print(i,"*",num,"=",i*num)
    i=i+1;

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-16:
Program to Display Characters from A to Z Using Loop.

input:

output:
A B C D.......Z
a b c d.......z

Solution:
#Lower upper case-------------------------
for i in range(97,123): #for lower case
    print(chr(i),end=" ")

#Upper Case-----------------------------
print("\n")
for i in range(65,91): #for upper case
    print(chr(i),end=" ")

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-17:
Program to Display Factors of a Number.

input:
val=24

output:
1,2,3,4,6,8,12

Solution:
num=int(input("Please enter number: "))
i=1
while(i<=num):
    if (num%i==0):
        print(i,end=", ")
    i=i+1

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-18:
Program to Make a Simple Calculator.

input:
a=20
b=5

output:
addition=25
subtraction=15
multiplication=100
division=4

Solution:
def simpleCalcultor():
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a//b
    
    print("Addition-1: \nSubtraction-2: \nMultiplication-3: \nDivision-4: \nExit-5")
    num=int(input("select Any one: "))
    if(num==1):
        a=int(input("Enter firse number: "))
        b=int(input("Enter second number: "))
        output=add(a,b)
        print("Addition of two number: ",output)
        simpleCalcultor()

    elif(num==2):
        a=int(input("Enter firse number: "))
        b=int(input("Enter second number: "))
        output=sub(a,b)
        print("Subtraction of two number: ",output)
        simpleCalcultor()

    elif(num==3):
        a=int(input("Enter firse number: "))
        b=int(input("Enter second number: "))
        output=mul(a,b)
        print("Multiplication of two number: ",output)
        simpleCalcultor()

    elif(num==4):
        a=int(input("Enter firse number: "))
        b=int(input("Enter second number: "))
        output=div(a,b)
        print("Division of two number: ",output)
        simpleCalcultor()

    elif(num==5):
        exit()

    else:
        print("Please Enter valide input")
        simpleCalcultor()

simpleCalcultor()


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-19:
Program to Convert Binary Number to Decimal and vice-versa.

input:
Enter Binary val: 0b100
Enter Decimal val: 4

output:
Decimal val:  4
Binary val:  0b100

Solution:
#Binary to Decimal----------------------
bval=eval(input("Enter binary val: "))
print("Show binary val: ")

dval=int(bval)
print("Dicaml val: ",dval)

#Decimal to Binary:---------------------
dval=eval(input("Enter Decimal val: "))
print("Decimal val: ",dval)

bval=bin(dval)
print("Binary val: ",bval)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-20:
Program to Convert Octal Number to Decimal and vice-versa.

input:
Enter ortal number: 0o100
Enter decimalval: 10

output:
Decimal val:  64 
Octol val:  0o12

Solution:
#Octal to Decimal 
oval=eval(input("Enter number: "))
print("Octal val: ",oval)

ival=int(oval)
print("Decimal val: ",ival)

#Decimal to Octal
dval=int(input("Enter val: "))
print("Decimal val: ")
oval=oct(dval)
print("Octol val: ",oval)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-21:
Program to Convert Binary Number to Octal and vice-versa.

input:

output:

Solution:
#Binary to Decimal 
bval=eval(input("Enter Binary number: "))
print("Binary val: ",bval)

oval=oct(bval)
print("Decimal val: ",oval)


#Octal to Binary
oval=eval(input("Enter otcatl val: "))
print("octal val: ",oval)
bval=bin(oval)
print("Binary val: ",bval)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question:

input:

output:

Solution:



#------------------------------------------------------------#

