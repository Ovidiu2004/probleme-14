a=int(input("Dati nr. de linii="))
b=[]
#pe diagonala principala
sp=0
for i in range(0, a):
    c=[]
    for j in range(0,a):
        c.append(int(input('>')))
    b.append(c)
for i in range(0,a):
    for j in range(0,a):
        print(b[i][j], end=" ")
    print()
for i in range(0,a):
    sp+=b[i][i]
print('Suma elementelor de pe diagonala principala =', sp)
#pe diagonala secundara
ss=0
h=0
for i in b[::-1]:
    ss+=i[h]
    h+=1
print("Suma elementelor de pe diagonala secundara=", ss)
# mai jos de diagonala principala
sps=0
for i in range(0,a):
    for j in range(0,a):
        if i<j:
            sps+=b[i][j]
print("Suma elementelor aflate mai jos de diagonala principala=", sps)
#mai sus de diagonala principala
spj=0
for i in range(0,a):
    for j in range(0,a):
        if i>j:
            spj+=b[i][j]
print("Suma elementelor aflate mai sus de diagonala principala=", spj)
#mai sus de diagonala secundara
sss=0
for i in range(0,a):
    if(i+j)<(a-1):
         sss+=b[i][j]
print("Suma elementelor aflate mai sus de diagonala secundara=", sss) 
#mai jos de diagonala secundara
ssj=0
for i in range(0,a):
    if (i+j)>(a-1):
    
        ssj+=b[i][j]
print("Suma elemenetlor aflate mai jos de diagonala secundara=", ssj)


