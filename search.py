import random as rd
a= [ ]
b=0

for i in range(100):
    a.append(rd.randint(1,1000000))
a2= sorted(a)    
li = []
for i in a2:
  if i not in li:
    li.append(i)
print(li)

