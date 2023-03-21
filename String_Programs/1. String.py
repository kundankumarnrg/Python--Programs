#============================================================================================
>>Formate:
1.Question
2.Input
3.Output
4.Hints
5.Solution
#============================================================================================

#------------------------------------------------------------#
Question-1:
Write a program to reverse the given String.

input:
s1="python program lang"

output:
res=gnal margorp nohtyp

Solution:
str_val="python program lang"

#Type-1:------------------------------#
print(str_val[::-1])


#Type-2:------------------------------#
def rev_string(str_val):
    tem=""
    for i in range((len(str_val)-1),-1,-1):
        tem=tem+str_val[i]
    print(tem)
rev_string(str_val)


#Type-3:------------------------------#
def revse_string():
    s1="I am kumar kundan"[::-1]
    print(s1)
revse_string()

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-2:
Program to reverse order of words in given string.

input:
s1="Python is programming lang"

output:
res=lang programming is Python

Solution:
s1="Python is programming lang"
def rev_ord_word(s1):
    print(s1)
    lst=s1.split()
    print(' '.join(lst[::-1]))

rev_ord_word(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-3:
Program to reverse internal content of each word.

input:
s1="Python is programming lang"

output:
res=nohtyP si gnimmargorp gnal 

Solution:
s1="Python is programming lang"

def rev_word_content(s1):
    print(s1)
    lst=s1.split()
    tem=""
    for val in lst:
        tem=tem+val[::-1]+" "
    print(tem)

rev_word_content(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-4:
Program to reverse internal content of each even possition of word.

input:
s1="python is use to web application"

output:
res=nohtyp is esu to bew application

Solution:
s1="python is use to web application"
def reverse_even_poss_word(s1):
    print(s1)
    lst=s1.split(" ")
    tem=""
    for i in range(len(lst)):
        if i%2==0:
            tem=tem+lst[i][::-1]+" "
        else:
            tem=tem+lst[i][::]+" "
    print(tem)

reverse_even_poss_word(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-5:
find output following formate.

input:
s1="aaaabbbbcc"

output:
res=a4b4c2

Solution:
s1="aaaabbbbcc"
def dip_follwing_formate(s1):
    print(s1)
    tem=""
    for ch in sorted(set(s1)):
        c=0
        c=s1.count(ch)
        tem=tem+ch+str(c)
    print(tem)

dip_follwing_formate(s1

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-6:
Write a program to print characters at odd position and even position for the given String.

input:
s1="PYTHON IS WEB DEVELOPEMENT PROGRAMMING LANGUAGE"

output:
Even possition val:  PTO SWBDVLPMN RGAMN AGAE
Odd possition val:  YHNI E EEOEETPORMIGLNUG

Solution:
s1="PYTHON IS WEB DEVELOPEMENT PROGRAMMING LANGUAGE"

def display_odd_even_poss_val(s1):
    print(s1)
    even,odd="",""
    for i in range(len(s1)):
        if i%2==0:
            even=even+s1[i]
        else:
            odd=odd+s1[i]
    print("Even possition val: ",even)
    print("Odd possition val: ",odd)

display_odd_even_poss_val(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-7:
Program to merge characters of 2 strings into a single string by taking characters alternatively

input:
s1="ravi" s2="teja"

output:
res='rtaevjia'

Solution:
s1="ravi" 
s2="teja"
def two_string_merze(s1,s2):
    tem=""
    for i in range(len(s1)):
        tem=tem+s1[i]+s2[i]
    print(tem)

two_string_merze(s1,s2)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-8:
Write a program to sort the characters of the string and first alphabet symbols followed by numeric values.

input:
s1="B4A1D3"

output:
res=ABCD134

Solution:
s1="B4A1D3"

def sort_char_number(s1):
    print(s1)
    ch_val=""
    int_val=""
    for ch in s1:
        if ch.isalpha():
            ch_val=ch_val+ch
        else:
            int_val=int_val+ch
    output=ch_val+int_val
    print(output)

sort_char_number(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-9:
Write a program for the following requirement.

input:
s1= "a4b3c2"

output:
res=aaaabbbcc

Solution:

s1="a4b3c2"
def disp_following_formate(s1):
    print(s1)
    output=""
    for ch in s1:
        if ch.isalpha():
            tem=ch
        else:
            output=output+(tem*int(ch))
    print(output)
disp_following_formate(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-10:
Write a program to perform the following.

input:
s1="a4k3b2"

output:
res="aeknbd"

Solution:
s1="a4k3b2"
def following_formate(s1):
    print(s1)
    output=""
    for ch in s1:
        if ch.isalpha():
            tem=ch
        else:
            output=output+tem+(chr((ord(tem))+int(ch)))
    print(output)

following_formate(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-11:
Write a program to remove duplicate characters from the given input string.

input:
s1="ABCDEFABCDEFFEECCDDDDEEF"

output:
res=ABCDEF

Solution:
s1="ABCDEFABCDEFFEECCDDDDEEF"

#Type-1-------------------------------------#
def remove_duplicat_element(s1):
    print(s1)
    uni_val=(''.join(sorted(set(s1))))
    print(uni_val)
remove_duplicat_element(s1)


#Type-2:-----------------------------------#
def rem_duplicat_val(s1):
    print(s1)
    uni_val=""
    for val in s1:
        if val not in uni_val:
            uni_val=uni_val+val
    print(uni_val)

rem_duplicat_val(s1)


#Type-3:----------------------------------#
def rem_element(s1):
    print(s1)
    lst=[]
    for ch in s1:
        if ch not in lst:
            lst.append(ch)
    print(''.join(lst))
rem_element(s1)


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-12:
Write a program to find the number of occurrences of each character present in the given String.

input:
s1=ABCABCABBCDE

output:
res=A-3,B-4,C-3,D-1,E-1

Solution:
s1="ABCABCABBCDE"

#Type-1:----------------------------#

def char_occurrences(s1):
    print(s1)
    for ch in sorted(set(s1)):
        c=0
        c=s1.count(ch)
        print(ch,"-",c,end=", ")
char_occurrences(s1)


#Type-2:---------------------------#
def charecter_occurence(s1):
    dic={}
    for val in s1:
        dic[val]=dic.get(val,0)+1
    print(dic)

charecter_occurence(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-13:
Check the string is anagram or not.

input:
case-1:
s1='earth'
s2='heart'

case-2:
s1='earth'
s2='heartt'

output:
res1=Annagram
res2=Not annagram

Hints:
if character lenght and all character are same then annagram.
ex:
    s1="ABCD" s2="BCDA"
    lenght=4
    all characters are same, Sequence is not important.

Solution:

s1='earth'
s2='heartt'
def Annagram(s1,s2):
    if len(s1)==len(s2):
        if(sorted(s1)==(sorted(s2))):
            print("Annagram")
        else:
            print("Not anngram")
    else:
        print("Not Annagram")
Annagram(s1,s2)


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-14:
Convert all string in upper case.

input:
s1="python"

output:
res="PYTHON"

Solution:
s1="python programming"
def uppercase(s1):
    print(s1)
    print(s1.upper())
    
uppercase(s1)


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-15:
convert all string in lower case.

input:
s1="DJANGO IS USE TO WEB DEVELOPMENT"

output:
res=django is use to web development

Solution:
s1="DJANGO IS USE TO WEB DEVELOPMENT"

def lowercase(s1):
    print(s1)
    print(s1.lower())

lowercase(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-16:
Each word first letter upper case.

input:
s1="Each word first letter upper case"

output:
res=Each Word First Letter Upper Case

Solution:
s1="Each word first letter upper case"
def first_litter_upper_case(s1):
    print(s1)
    print(s1.title())

first_litter_upper_case(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-17:
String first letter upper case.

input:
s1="sentence first letter upper case"

output:
res=Sentence first letter upper case

Solution:
s1="sentence first letter upper case"

def first_letter_upper(s1):
    print(s1)
    print(s1.capitalize())

first_letter_upper(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-18:
Each word first and last char uppper case.

input:
s1="sentence first letter upper case"

output:
res=SentencE FirsT LetteR UppeR CasE 

Solution:
def first_last_upper_case(s1):
    print(s1)
    tit=s1.title()
    lst=tit.split(" ")
    tem=""
    for val in lst:
        tem=tem+val[:len(val)-1]+val[-1].upper()+" "
    print(tem)
    
first_last_upper_case(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-19:
find out duplicate characters and how many time comes.

input:
s1="find out duplicate charecter and how many time comes"

output:
All duplicate val: 
 GDKFCASBHJIE

Occurrence duplicat val:
  {'A': 4, 'B': 2, 'C': 2, 'D': 6, 'F': 6, 'I': 3, 'S': 5, 'K': 3, 'J': 4}

Solution:
s1="ABCDEFGHIABACDIIDFDSKFJSADJFKSJDFKSJFS"
def findout_duplicate(s1):
    dup=""
    val=set(s1)
    for value in val:
        if value in s1:
            dup=dup+value
    print("All duplicate val: \n",dup)

    dic={}
    dic2={}
    for data in s1:
        dic[data]=dic.get(data,0)+1
    for k,v in dic.items():
        if v>1:
            dic2[k]=v
    print("\nOccurrence duplicat val:\n ",dic2)

findout_duplicate(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-20:
Maximum occurring character.

input:
s1="Maximum occurring character"

output:
Maximum occurring character: c --> 4

Solution:
s1="Maximum occurring character"

def max_occuring_char(s1):
    dic={}
    key=""
    val=""
    tem=1
    for i in s1:
        dic[i]=dic.get(i,0)+1
    for k,v in dic.items():
        if v>tem:
            key,val=k,v
            tem=val
    print(dic)
    print("Maximum occurring character: ",key,"-->",val)

max_occuring_char(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-21:
find out vowel in given string.

input:
s1="find out vowel in given string"

output:
Show avilable vowel in string:  eiou

Solution:
s1="find out vowel in given string."
def show_vowel(s1):
    tem="aeiouAEIOU"
    vow=""
    for ch in tem:
        if ch in s1:
            vow=vow+ch
    print("Show avilable vowel in string: ",vow)

show_vowel(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-22:
vowel count in string.

input:
s1="vowel count in string"

output:
e-1, i-2, o-2, u-1,

Solution:
s1="vowel count in string"
def vowel_count(s1):
    tem='aeiouAEIOU'
    output=""
    c=0
    for ch in tem:
        if ch in s1:
            c=0
            c=s1.count(ch)
            if c>0:
             output=output+ch+"-"+str(c)+", "
    print(output)

vowel_count(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-23:
Sort the charecter of in the string.

input:
s1="kdfsjfjksnmnmcuiorekvnm"

output:
res=cdeffijjkkkmmmnnnorssuv

Solution:
s1="kdfsjfjksnmnmcuiorekvnm"
def sort_string(s1):
    print(s1)
    lst=list(s1)
    print(''.join(sorted(lst)))
sort_string(s1)

#------------------------------------------------------------#


#------------------------------------------------------------#
Question-24:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-25:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-27:


input:


output:


Solution:


#------------------------------------------------------------#


#------------------------------------------------------------#
Question-28:


input:


output:


Solution:


#------------------------------------------------------------#

