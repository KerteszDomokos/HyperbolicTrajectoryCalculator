"""
Copyrighth
    Kertész Domokos
    kerteszdomokos@gmail.com
Projekt: Hyperbolic function
Verzió:v1.1
"""
import math as mt

helpHUN='''
r0 az az x koordináta, ahol az x tengelyt metszi a hiperbola
l az az y koordináta, ahol az y tengelyt metszi a hiperbola
'''

print('Start the hyperbolic function datas calculator - Kertész Domokos 2021')

print('Example datas (for more see the example dictionary): rp=1.6, l=4.5, x=1.052, y=6.24')


#request values - see the example datas dictionary
try:
    rp=float(input ('R0 (use . not ,) = '))
except:
    print('Error in input')
    rp=0
try:
    l=float(input('l (use . not ,) = '))
except:
    print('Error in input')
    l=0

RPpL=l/rp
e=RPpL-1#calculate eccentricity
#r0=a(e-1)
a=rp/(e-1)
c=a*e
b=mt.sqrt(c**2-a**2)

print("\t    Inputs\nrp:\t",rp,'\t l:\t',l)
print('\n\t  Results')
print('Eccentricity:\t',e)
print("'a' value\t",a)
print("'b' value\t",b)
print("'c' value\t",c)

#load the x val
try:
    x=float(input('x coordinate (use . not ,): '))
except:
    print('Error in inpu')
    x=0

#1=x**2/a**2-y**2/b**2
xpa=(x-c)**2/a**2
#1=xpa-y**2/b**2
y=mt.sqrt(-b**2 * (a**2 - (x-c)**2))/a

print('  Results coordinates')
print('x:\t',x)
print('y:\t(+-)~',y)

inp=input ('If you know the y coordinate write this here (if not press enter):')
if inp!='':
    real_y=float(inp)
    delta=mt.sqrt((y-real_y)**2)
    sz=delta/real_y*100
    print('Error different %:\t', round(sz,1),'%')
    print('Error different:\t', delta)

print('\nA kimenet pontossága nagyon függ a bevitt adatok, pontosságától, és a pontok szórásától!')

input('end')
