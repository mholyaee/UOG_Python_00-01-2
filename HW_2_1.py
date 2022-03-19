a=float(input())
b=float(input())
c=float(input())
if a==b==0:
    print('IMPOSSIBLE')
elif a==0 and b!=0:
    print("%.3f" %(-c/b))
else:
    d=b**2-4*a*c
    if d>0:
        x1=(-b+d**0.5)/(2*a)
        x2=(-b-d**0.5)/(2*a)
        if x1>x2:
            x1,x2=x2,x1
        print("%.3f" % x1)
        print("%.3f" % x2)
    elif d==0:
        x1=-b/(2*a)
        print("%.3f" % x1)
    else:
        print('IMPOSSIBLE')
