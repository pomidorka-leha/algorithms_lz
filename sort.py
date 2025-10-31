import random as rd
a= [ ]
b=0

for i in range(10):
    a.append(rd.randint(1,100))
a2 = a.copy()    
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            b +=1    
    print('список с шагом',a)        
print('количество всех перестановок у пузырька',b)    
rt=0
d=0 
while d < len(a2) - 1:
    mim = d
    g = d + 1
    while g < len(a2):
        if a2[g] > a2[mim]:
            mim=g
        g += 1
    rt += 1
    a2[d], a2[mim] = a2[mim], a2[d]
    d +=1
    print('список выбором',a2)
    
print('количество операций выбором',rt)    