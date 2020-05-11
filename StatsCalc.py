from math import sqrt

def SUMxx(SumX,Sum2X,n):
    Sxx = Sum2X - (pow(SumX,2)/n)
    return Sxx
def SUMyy(SumY,Sum2Y,n):
    Syy = Sum2Y - (pow(SumY,2)/n)
    return Syy
def SUMxy(SumX,SumY,SumXY,n):
    Sxy = SumXY - ((SumX*SumY)/n)
    return Sxy
def rCoeff(Sxx,Syy,Sxy):
    r = Sxy /(sqrt(Sxx*Syy))
    return r

def bCoeff(Sxx,Sxy):
    return Sxy/Sxx

def aCoeff(b,SumX,SumY,n):
    MeanX = SumX/n
    MeanY = SumY/n
    a = MeanY - (b*MeanX)
    return a

Xtot = Ytot = []
XtotS = YtotS = False
entry = list(input('Σx-0  Σy-1  Σxy-2  Σx²-3  Σy²-4  n-5  x-6  y-7  Sxx-8  Syy-9  Sxy-10\nEnter the options:'))
relationship = ['Σx','Σy','Σxy','Σx²','Σy²','n','x','y','Sxx','Syy','Sxy','r','a','b']
check = [ True if str(i) in entry else False for i in range(len(relationship))]

All = [0 for i in range(len(relationship))]

All[5] = int(input('Enter n: '))
check[5] = True


if check[8]:
    All[8]  = float(input('Enter Sxx: '))
elif check[0] and check[3] and check[5]:
    All[0] = float(input('Enter Σx: '))
    All[3] = float(input('Enter Σx²: '))
    All[8] = SUMxx(All[0],All[3],All[5])
elif check[6]:
    XtotS = True
    for i in range(All[5]):
        x = float(input('Enter the val for x:'))
        All[0] += x
        All[3] += pow(x,2)
        Xtot.append(x)
    All[8] = SUMxx(All[0],All[3],All[5])
print(f'Sxx = {All[8]}')
check[8] = True

if check[9]:
    All[9]  = float(input('Enter Syy: '))
elif check[1] and check[4] and check[5]:
    All[1] = float(input('Enter Σy: '))
    All[4] = float(input('Enter Σy²: '))
    All[9] = SUMyy(All[1],All[4],All[5])
elif check[6]:
    YtotS = True
    for i in range(All[5]):
        y = float(input('Enter the val for y:'))
        All[1] += y
        All[3] += pow(y,2)
        Ytot.append(y)
    check[5] = True
    All[9] = SUMyy(All[1],All[3],All[5])

print(f'Syy = {All[9]}')
check[9] = True


if check[10]:
    All[10]  = float(input('Enter Sxy: '))
elif check[0] and check[1] and check[2] and check[5]:
    All[2] = float(input('Enter Σxy: '))
    All[1] = float(input('Enter Σy: '))
    All[0] = float(input('Enter Σx: '))
    All[10] = SUMxy(All[0],All[1],All[2],All[5])
elif check[2]:
    if not XtotS and YtotS:
        for i in range(All[5]):
            x = float(input('Enter the val for x:'))
            y = Ytot[i]
            All[2] += x*y
            All[0] += x 
        All[1] = sum(Ytot)
    elif XtotS and not YtotS:
        for i in range(All[5]):
            x = Xtot[i]
            y = float(input('Enter the val for y:'))
            All[2] += x*y
            All[1] += y
        All[0] = sum(Xtot)
    elif XtotS and YtotS:
        for i in range(All[5]):
            x = Xtot[i]
            y = Ytot[i]
            All[2] += x*y
        All[0] = sum(Xtot)
        All[1] = sum(Ytot)
    else:
        for i in range(All[5]):
            x = float(input('Enter the val for x:'))
            y = float(input('Enter the val for y:'))
            All[2] += x*y
    check[0] = check[1] = True
    All[10] = SUMxy(All[0],All[1],All[2],All[5])


check[10] = True

All[11] = rCoeff(All[8],All[9],All[10])
All[12] = bCoeff(All[8],All[10])
All[13] = aCoeff(All[12],All[0],All[1],All[5])
check[11]=check[12]=check[13]=True

for i in range(len(relationship)):
    if check[i]:
        print(f'{relationship[i]}:{All[i]}')