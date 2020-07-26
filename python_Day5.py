#!/usr/bin/env python
# coding: utf-8

###### Q[1]-:


a=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]

a.sort()
print("sorted list is-->",a)

for each in a:
    if each==0:
        a.remove(each)
        a.append(each)
    
print("new List is-->",a)


####### Q[2]-:


list1=[10,20,40,60,70,80]
list2=[5,15,25,35,45,60]
list3=list1+list2
print("After merging two sorted list-->",list3)
x=0
while x<len(list3)-1:
    if list3[x]>list3[x+1]:
        list3[x],list3[x+1]=list3[x+1],list3[x]
        x=-1
    x=x+1
print(list3)

