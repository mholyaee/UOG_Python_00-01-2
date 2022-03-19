i=1
Sum=0
sgn=1
while i<=99:
    Sum+=i/(i+1)*sgn
    sgn*=(-1)
    i+=1
print(Sum)
