# -*- coding: utf-8 -*-
"""Assignment 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zSxSK5BONYmQI_mghIlBDqXfmlx1gCEn

# CSE110 Lab Assignment 3 (String)

This Assignment is to help you develop your concept of Strings in Python.

**<font color='red'>[Please follow variable naming conventions including using meaningful variable names for all the tasks]</font>**\
<font color='red'>When you run your code, please make sure your outputs exactly match the sample outputs for each of the sample inputs given. Check if your code works for other valid inputs not given in the samples.</font>

## Write the code in Python to do the following tasks:

### Task 1

Write a Python program that takes a String as an input from the user and prints that String in **reverse** order.

**<font color='red'>You cannot use the built-in reverse() function for this task.**

=====================================================================

**Sample Input 1:**\
 CSE110

**Sample Output 1:**\
 011ESC

=====================================================================

**Sample Input 2:**\
Python

**Sample Output 2:**\
nohtyP

=====================================================================

**Sample Input 3:**\
1576527  

**Sample Output 3:**\
7256751

=====================================================================
"""

x= str(input("Enter a string: "))
print(x[::-1])

"""### Task 2

Write a python program that takes 2 inputs from the user, where the first input is a string with length greater than 1. The second input is the index of the first given string from where you have to start reversing. After reversing the first input string from that index, print the new string back to the user. See samples below for clarification.

=====================================================================

**Sample Input 1:**

72418

4

**Sample Output 1:**

81427


**Explanation**: Our second input, index '4' is the last index of our first input String '72418', hence the entire string is reversed giving us '81427'.

=====================================================================

**Sample Input 2:**

12345

2

**Sample Output 2:**

32145

**Explanation**: The second input is '2' so we have to reverse from index 2 of our first input. The 2nd index of our first input String is '3', index 1 is '2' and index 0 is '1'. Hence, if we reverse indexes 0 to 2, we get '321'. Index 3 and 4 which is '4' and '5' respectively remains unchanged hence our final output is '32145'.

=====================================================================

**Sample Input 3:**

aBcd1234defg

5

**Sample Output 3:**

21dcBa34defg

**Explanation**: From our first input String 'aBcd1234defg',

index 0 = 'a'

index 1 = 'B'

index 2 = 'c'

index 3 = 'd'

index 4 = '1'

index 5 = '2'

index 6 = '3'

Since our second input is 5, index 0 to index 5 is reversed and we have '21dcBa' and the rest is unchanged from indexes 6 to 11 ('34defg'). Therefore, we have '21dcBa34defg' finally.

=====================================================================

"""

x= str(input("Enter a string: "))
num= int(input("Enter a number: "))
print((x[num::-1])+(x[num+1:]))

x= input("Enter a string ")
bool= False
for y in x:
  if (y=="0" or y=="1"):
    pass
  else:
   bool=True
if (bool==True):
  print("Not a Binary Number")
else:
  print("Binary Number")

"""### Task 4

Write a Python program that will ask the user to enter a  word as an input.

* If the length of the input string is less than 4, then your program should print the same string as an output.
* If the input string’s length is greater than 3, then your program should add "er" at the end of the input string.
* If the input string already ends with "er", then add "est" instead, regardless of the length of the input string
* If the input string already ends with "est", then your program should print the same input string as an output.

=====================================================================

**Sample Input 1**:\
strong

**Sample Output 1**:\
stronger

**Explanation**: Length of input = 6, not less than 4, greater than 3, does not end with "er" or "est", therefore "er" is added making "strong", "stronger".

=====================================================================

**Sample Input 2**:\
stronger

**Sample Output 2**:\
strongest

**Explanation**: Input string ends with "er", therefore "er" is replaced with "est" instead so we have "strongest" from "stronger".

=====================================================================

**Sample Input 3**:\
strongest

**Sample Output 3**:\
strongest

**Explanation**: Our input here already ends with "est" so the same input i.e. "strongest" is printed.

=====================================================================

**Sample Input 4**:\
abc

**Sample Output 4**:\
abc

**Explanation**: Since length of input string is less than 4, the given input is printed as output.

=====================================================================

**Sample Input 5**:\
ber

**Sample Output 5**:\
best

**Explanation**: Although the length of the input string is 3 which is less than 4, but it ends with er so we ignore the length and replace "er" with "est" regardless.

=====================================================================
"""

x= input("Enter a string: ")
if x.endswith("er"):
    print(x[:-2]+"est")
elif x.endswith("est"):
    print(x)
elif (len(x)<4):
    print(x)
elif (len(x)>3):
    print(x+"er")

"""
### Task 5

Write a Python program that will ask the user to input a string (containing exactly one word). Then your program should print subsequent substrings of the given string as shown in the examples below.

=====================================================================

**Hints(1):** You may use "for loop" for this task.

**Hints(2):** You may use print() function for printing newlines.

For example:\
print(1)\
print(2)

Output:\
1\
2

=====================================================================

We can use print(end = "") to skip printing the additional newline.

For example:\
print(1, end ="")\
print(2)

Output:(prints the following output right next to the previous one)\
12

=====================================================================

**Sample Input 1**:\
BANGLA

**Sample Output 1**:\
B\
BA\
BAN\
BANG\
BANGL\
BANGLA

**Explanation**: The length of the string is 6 so there are 6 lines where in each line a substring of the input string, of length equal to the line number is printed i.e. substring with only the letter "B" printed in the first line, substring "BA" of length 2 printed in the 2nd line, "BAN" length of which is 3 being printed in the 3rd line and so on.

=====================================================================

**Sample Input 2**:\
DREAM

**Sample Output 2**:\
D\
DR\
DRE\
DREA\
DREAM

**Explanation**: Simply, no of lines = length of the input string and no of letters in each line = line number.

=====================================================================




"""

x=input("Enter a string: ")
for i in range(1,len(x)+1):
  print(x[:i])

"""### Task 6

Write a Python program that will ask the user to input a string (containing exactly one word). Then print the ASCII code for each character in the String using the ord() function.

To check if your program is working correctly or not, you can find a list of all correct values from the following website. You may look at “Dec” and “Char” columns only and ignore the other columns for this problem.\
link: http://www.asciitable.com/

=====================================================================

**Sample Input 1**:\
Programming

**Sample Output 1**:\
P : 80\
r : 114\
o : 111\
g : 103\
r : 114\
a : 97\
m : 109\
m : 109\
i : 105\
n : 110\
g : 103

**Explanation**: Each line prints a letter sequentially from the given string and its corresponding ASCII value separated by " : ".

=====================================================================

**Sample Input 2**:\
hunger

**Sample Output 2**:\
h : 104\
u : 117\
n : 110\
g : 103\
e : 101\
r : 114

**Explanation**: Same as previous.

=====================================================================
"""

x=input("Enter a string: ")
for i in x:
  print(i,":",ord(i))

"""### Task 7

Write a Python program that takes a string as an input from the user containing all small letters and then prints the next alphabet in sequence for each alphabet in the input.

*Hint: You may need to use the functions ord() and chr(). The ASCII value of ‘a’ is 97 and ‘z’ is 122.*

=====================================================================

**Sample Input 1:**\
abcd

**Sample Output 1:**\
bcde

=====================================================================

**Sample Input 2:**\
the cow

**Sample Output 2:**\
uif!dpx

=====================================================================

<font color='red'>[Must fulfil this criteria]</font>

**Sample Input 3:**\
xyzabc

**Sample Output 3:**\
yzabcd

=====================================================================

"""

x=input("Enter a string: ")
b=" "
for i in x:
  a=ord(i)
  if a==ord("z"):
    b+="a"
  else:
    b+=chr(a+1)
print(b)

x=input()
i=0
store=''
while i<len(x):
    if x[i]=='z':
        store+='a'
    else:
        store=store+chr(ord(x[i])+1)
    i+=1
print(store)

"""### Task 8

Write a Python program that takes a String as input from the user, removes the characters at even index and prints the resulting String in uppercase without using the built-in function upper().

=====================================================================

**Sample Input 1**:

String

**Sample Output 1**:

TIG

**Explanation**: The characters 'S', 'r' and 'n' are at index positions 0, 2, and 4 respectively. Hence they are removed and the remaining characters 'tig' are capitalized giving us output 'TIG'.

=====================================================================

**Sample Input 2**:

abcd

**Sample Output 2**:

BD

**Explanation**: Only the characters at the odd indices, 1 and 3, 'b' and 'd' are captitalized, concatenated and printed.

=====================================================================

"""

x=input("Enter a string: ")
a=" "
for i in range(0,len(x)):
  if (i%2!=0):
    a+= chr(ord(x[i])-32)
print(a)

x=input()
i=0
store=''
while i<len(x):
    if i%2!=0:
        if 65<=ord(x[i])<=90:
            store+=x[i]
        else:
            store+=chr(ord(x[i])-32)
    i+=1
print(store)

"""### Task 9

Write a python program that splits a given string on a given split character. The first input is a String and the second input is the character that will be used to split the first String.

<font color='red'>[You cannot use the built-in split function for this task]</font>

=====================================================================

**Sample Input 1:**<br/>
This-is-CSE110<br/>
-<br/>

**Sample Output 1:**<br/>
This<br/>
is<br/>
CSE110

**Explanation**: The second input which is the character '-', is used to split or divide the first input String 'This-is-CSE110' into 'This', 'is' and 'CSE110' which are printed individually in separate lines.

=====================================================================

**Sample Input 2**:\
tom@gmail,harry@yahoo,bob@gmail,mary@gmail

,

**Sample Output 2**:

tom@gmail

harry@yahoo

bob@gmail

mary@gmail

=====================================================================
"""

x= input("Enter a string: ")
y= input("Enter a character: ")
a= " "
for i in x:
  if i==y:
    print(a)
    a=" "
  else:
    a+=i
print(a)

"""### Task 10
Given a string, create a new string with all the **consecutive duplicates removed**.

**Hint:** You may make a new string to store the result. You can check whether the current character and the next character are the same, then add that character to the new string.

**Note**: Only consecutive letters are removed not all duplicate occurences of a letter. You may try doing this alternative i.e. removing all duplicate letters from a given string, for your own practice.

=====================================================================

**Sample Input 1**:\
AAABBBBCDDBBECE

**Sample Output 1:**\
ABCDBECE

**Explanation**: From the 3 consecutive "A"s, 2 are removed and we have 'A' only. Then from the 4 consecutive 'B's, 3 are removed and only one is added to the new string giving us "AB". Since we have only one 'C' next, it is added making the resulting string "ABC" now and so on.

=====================================================================

**Sample Input 2**:\
Jupyter Notebook is better. Case sensitivity check AAaaaAaaAAAa.

**Sample Output 2:**\
Jupyter Notebok is beter. Case sensitivity check AaAaAa.

**Explanation**: Just the 2 consectutive 'o's and 't's are changed to one at first and the uppercase 'A' and lowercase 'a' are treated separately i.e. case sensitive when checking for consecutive duplicates.

"""

x=input("Enter a string: ")
a=" "
for i in x:
  if a==" " or i!=a[len(a)-1]:    # the last letter of the string of store
    a+=i
print(a)

"""### Task 11

Write a python program that takes 2 inputs from the user. The first input is a string and the second input is a letter. The program should remove all occurences of the letter from the given string and print the output. If the letter is not found in the string and the length of string is greater than 3, then remove the first letter and last letter of the given string and print it. Otherwise print the string as it is. You can assume that all the input will be in lowercase letter.

=====================================================================


**Sample Input 1**:\
tanjiro kamado\
a

**Sample output 1**:\
tnjiro kmdo

**Explanation**: All 3 instances of the character 'a' is removed from the input String 'tanjiro kamado' to give us output 'tnjiro kmdo'.

=====================================================================

**Sample Input 2**:\
eren yeager\
k


**Sample Output 2**:\
ren yeage

**Explanation**: The character 'k' is absent in the first input String 'eren yeager' and it's length is 11 which is greater than 3 therefore the first character 'e' and the last character 'r' is removed. Hence, the final String is 'ren yeage'.

=====================================================================

**Sample Input 3:**\
hi\
a

**Sample Output 3:**\
hi

**Explanation**: The letter 'a' is not found in our first input 'hi', the length of which is 2. Since the character is not present and the length is less than 3, we print the String 'hi' as it is.

=====================================================================

"""

x= input("Enter a string: ")
y= input("Enter a letter: ")
a=""
for i in x:
  if y==i:
    pass
  else:
     a+=i
if len(x) <= 3:
  print(x)
elif x==a:
  print(x[1:-1])
else:
  print(a)

"""### Task 12

Write a Python program that will take one input from the user made up of two strings separated by a comma and a space (see samples below). Then create a mixed string with alternative characters from each string. Any leftover chars will be appended at the end of the resulting string.

*Hint: For adding the leftover characters you may use string slicing.*

**Note:** Please do not use lists for this task.

=====================================================================

**Sample Input 1:**\
ABCD, efgh

**Sample Output 1:**\
AeBfCgDh

**Explanation**: At first, the two strings divided by ", " should be separated. Then the first character of the first string 'A' is concatenated with the first character of the second string 'e' which in turn is concatenated to the second character of the first string 'B', the second character of the second string f and so on since the strings are of equal length.

=====================================================================

**Sample Input 2:**\
ABCDENDFGH, ijkl

**Sample Output 2:**\
AiBjCkDlENDFGH

**Explanation**: Here, since the length of the first string is greater than the length of the second string, after separation, the characters are concatenated alternatively as in sample input/output 1, till the length of the second string i.e. ijkl. Since, there are no more characters in the second string after that, the remaining characters if the first string i.e. ENDFGH in this case are concatenated at the end of the final string.

=====================================================================

**Sample Input 3:**\
ijkl, ABCDENDFGH

**Sample Output 3:**\
iAjBkClDENDFGH

**Explanation**: This time, the length of the second string is greater than the length of the first string therefore the first letters of the 2 strings 'i' and 'A', then the second letters 'j' and 'B' and so on are being concatenated until there are no more letters in the first shorter string following which the remaining letters i.e. ENDFGH again in this case too (this may be different for other different string inputs) are added at the end giving us the resulting output string.

=====================================================================

"""

x=input()
i=0
s1,s=x.split(',')
i=0
s2=''
while i<len(s):  #line 4-9 are for removing the space from the second string
    if s[i]!=' ':
        s2+=s[i]
    i+=1
a=0
b=0
mixed_strring=''
while a<len(s1) and b<len(s2):
    mixed_strring+=s1[a]+s2[b]
    a+=1
    b+=1
if a<len(s1):   # line 17-20 for the leftover letter
    mixed_strring+=s1[a:len(s1)]
else:
    mixed_strring+=s2[b:len(s2)]

print(mixed_strring)

"""## Optional Tasks (13 - 15) [Ungraded]

### Task 13

Suppose you are given two strings, s1, and s2. Now, print a new string made up of the last characters and then the first characters of the input strings.

=====================================================================

**Sample Input 1**:

s1 = new

s2= string

**Sample Output 1**:

gwsn

**Explanation:** The last character of the String s2 is 'g'. The last character of the String s1 is 'w'. The first character of the String s2 is 's'. The first character of the String s1 is 'n'. Together they give us the ouput we want 'gwsn'.

=====================================================================

**Sample Input 2**:

s1 = abcd

s2= efgh

**Sample Output 2**:

hdea

**Explanation:** The last characters of the Strings s2 and s1 is 'h' and 'd' respectively while the first characters of the Strings is 'e' and 'a' respectively. Together they give us the ouput we want 'gwsn'.

=====================================================================
"""

s1 = 'new'
s2= 'string'
print(s2[-1]+s1[-1]+s2[0]+s1[0])

"""### Task 14

Write a python program that takes two inputs. The first input is a string and the second input is a number. If the number is even then concatenate the given string two times the given number and if the number is odd then concatenate the given string three times the given number.

=====================================================================

**Sample Input 1**:

CSE110

4

**Sample output 1**:

CSE110CSE110CSE110CSE110CSE110CSE110CSE110CSE110

**Explanation**: The second input which is the number 4 is even, therefore the first string input 'CSE110' is concatenated(joined together) 4*2 = 8 times.

=====================================================================

**Sample Input 2**:

CSE110

3

**Sample Output 2**:

CSE110CSE110CSE110CSE110CSE110CSE110CSE110CSE110CSE110

=====================================================================

"""

x1=input()
x2=int(input())
if x2%2==0:
   print(x1*(x2*2))
else:
    print(x1*(x2*3))

"""### Task 15

Write a python program that takes a string as an input from the user and then modifies the string in such a way that the string always starts with an uppercase letter and the case of each subsequent letter is the opposite of the previous letter (uppercase character followed by a lowercase character followed by an uppercase character and so on).  Finally the modified string is printed to show the user.

*Hint:  Flags/counters can be used to manage uppercase-lowercase.*

=====================================================================

**Sample Input 1:**\
Python programming is very easy

**Sample Output 1:**\
PyThOn PrOgRaMmInG iS vErY eAsY

=====================================================================

**Sample Input 2:**\
I&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     love       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Programming

**Sample Output 2:**\
I&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     lOvE       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pYtHoN&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pRoGrAmMiNg

=====================================================================

**Sample Input 3:**\
CSE110 Course

**Sample Output 3**\
CsE110 cOuRsE



=====================================================================

**Sample Input 4:**\
c

**Sample Output 4:**\
C

=====================================================================

"""

a=input()
count=0
b=''
for i in a:
  if i==' ' or i.isdigit():
     b=b+i
  else:
    if count%2==0:
      b=b+i.upper()
    else:
      b=b+i.lower()
    count+=1
print(b)