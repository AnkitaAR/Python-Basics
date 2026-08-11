num=input("Please enter a number (numerator)")
num=int(num)
den=input("Please enter a number (denominator)")
den=int(den)
if num%den==0:
    print(num," is completely divisible by ",den)
else:
    print(num," is completely not divisible by ",den)
    