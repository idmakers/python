
import math

num1 = [1,3]
num2 = [2,4]
num1.extend(num2)
print (num1)
num1.sort()
print(num1)
if len(num1)%2 !=0 :
    mid = num1[math.ceil(len(num1)/2)-1]
    print(mid)
else :
    mid =   (num1[math.ceil(len(num1)/2)-1]+num1[math.ceil(len(num1)/2)])/2
    print(mid)
