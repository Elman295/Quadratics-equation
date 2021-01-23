import math   # import

"""
   ax**2 + b*x +c
   
"""


a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

delta=(b*b)-(4*a*c)

if delta>0:
    result1=(-b+math.sqrt(delta))/(2*a)
    result2=(-b-math.sqrt(delta))/(2*a)

    print(f"First answer is {result1}"
          f"   Second answer is {result2}")

elif delta==0:
    result=(-b)/(2*a)
    print(f" your answer is {result}")
else:
    print("you dont have any answer ")
