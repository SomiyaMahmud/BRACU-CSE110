# -*- coding: utf-8 -*-
"""Assignment 7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PjMxzLHBZKNRy1ZbyLl9oJugR3fw5pSD
"""

#1
list1 = [5,2,0,7,1,4,6,3]
for i in range(len(list1)):
  for j in range(0,len(list1)-i-1):
    if list1[j]>list1[j+1]:
      temp=list1[j]
      list1[j]=list1[j+1]
      list1[j+1]=temp
print(list1)

#2
my_list= [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
for i in range(len(my_list)):
  min=my_list[i]
  min_idx=i
  for j in range(i+1,len(my_list)):
    if my_list[j]<min:
      min=my_list[j]
      min_idx=j
  temp=my_list[min_idx]
  my_list[min_idx]=my_list[i]
  my_list[i]=temp
print(my_list)

#3
my_list= [10, 1, 20, 3, 6, 2, 5, 11, 15, 2, 12, 14, 17, 18, 29]
for i in range(len(my_list)):
  max=my_list[i]
  max_idx=i
  for j in range(i+1,len(my_list)):
    if my_list[j]>max:
      max=my_list[j]
      max_idx=j
  temp=my_list[max_idx]
  my_list[max_idx]=my_list[i]
  my_list[i]=temp
print(my_list)

#4
sitting_list = [10,30,20,70,11,15,22,16,58,100,12,56,70,80]
even=[]
odd=[]
for i in range(len(sitting_list)):
    if i%2==0:

        even.append( sitting_list[i])

    else:
        odd.append( sitting_list[i])
even=sorted(even)

odd=sorted(odd)

odd=odd[::-1]

even_count=0
odd_count=0
list1=[]
for j in range(len(sitting_list)):
  if j%2==0:
    list1.append(even[even_count])
    even_count+=1
  else:
    list1.append( odd[odd_count])
    odd_count+=1

print(list1)

#5
list1 = [ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]
a = input('Enter Desired Course Name: ')
x=0
if a == 'CSE110':
    x = 1
elif a == 'PHY111':
    x = 2
elif a == 'MAT110':
    x = 3
for i in range(len(list1)):
  min=list1[i][x]
  min_idx=i
  for j in range(i+1,len(list1)):
    if list1[j][x]>min:
      min=list1[j][x]
      min_idx=j
  temp=list1[min_idx]
  list1[min_idx]=list1[i]
  list1[i]=temp
for k in range(len(list1)):
  print(list1[k][0])

#Task-6
my_list = [4, 2, 3, 1, 6, 5]
a=my_list.copy()
count = 0
for i in range(len(my_list)-1):
  min=my_list[i]
  min_idx=i
  for j in range(i+1,len(my_list)):
    if my_list[j]<min:
      min=my_list[j]
      min_idx=j
  temp=my_list[min_idx]
  my_list[min_idx]=my_list[i]
  my_list[i]=temp
for k in range(len(my_list)):
  if a[k]==my_list[k]:
    pass
  else:
    count+=1
print(count)

#7
list1 = [1, 2, 1, 4]
list2 = [5, 4, 1]
merged_list1= list1 + list2
for i in range(len(merged_list1)):
  for j in range(0,len(merged_list1)-i-1):
    if merged_list1[j]>merged_list1[j+1]:
      temp=merged_list1[j]
      merged_list1[j]=merged_list1[j+1]
      merged_list1[j+1]=temp
print('Sorted list =',merged_list1)
a=len(merged_list1)
if a%2==0:
  median1=merged_list1[a//2]
  median2=merged_list1[a//2-1]
  median=(median1+median2)/2
else:
  median=merged_list1[a//2]
print('Median =',median)

#8
list1= [1, -8, 4, -7, -20, 26, 70, -85]
list2=[]
dic={}
min=0
for i in list1:
  for j in list1:
    sum=i+j
    if sum not in list2 and i!=j:
      list2.append(sum)
      dic[str(i)+','+str(j)]=sum
#print(dic)
list2.append(0)
list2.sort()
for k in range(len(list2)):
  if list2[k]==0:
    break
if list2[k+1]<list2[k-1]*-1:
  min=list2[k+1]
else:
  min=list2[k-1]
for i,j in dic.items():
  if j == min:
    print(i)

#8(alter)
list1=  [-10, 15, 2, 4, -4, 7, -8]

def bubble_sort(list_1):
  for i in range(len(list_1)-1):
    for j in range(len(list_1)-1-i):
      if list_1[j]>list_1[j+1]:
        temp=list_1[j]
        list_1[j]=list_1[j+1]
        list_1[j+1]=temp
def find_pair(list_1):
  dic={}
  for i in list_1:
    for j in list_1:
      if i!=j:
        dic[(i,j)]=abs(i+j)
  values_list=list(dic.values())
  bubble_sort(values_list)
  min=values_list[0]
  for key,value in dic.items():
    if value==min:
      return key
value1,value2=find_pair(list1)
print('Two pairs which have the smallest sum =', value1 ,'and', value2)

#9
import math
points = [(5,3), (2,9), (-2,7), (-3,-4), (0,6), (7,-2)]
#def distance(points):
list1=[]
for i in points:
   distance=math.sqrt(i[0]**2+i[1]**2)
   list1.append(distance)
list2=list1.copy()
for j in range(len(list1)):
   min=list1[j]
   min_idx=j
   for k in range(j+1,len(list1)):
     if list1[k]<min:
       min=list1[k]
       min_idx=k
   temp=list1[min_idx]
   list1[min_idx]=list1[j]
   list1[j]=temp
for l in range(len(list1)):
     if list1[0]==list2[l]:
       print(points[l])
       break
print('Minimum distance =',list1[0])