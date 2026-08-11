#accept marks from user
print("Enter marks of 5 subjects")
m1=int(input())
m2=int(input())
m3=int(input())
m4=int(input())
m5=int(input())

#calculating the avg
avg=(m1+m2+m3+m4+m5)/5

if avg>=80 and avg<=100:
    print("Your grade is A")
elif avg>=60 and avg<=79:
     print("Your grade is B")
elif avg>=35 and avg<=59:
     print("Your grade is C")
elif avg>=0 and avg<=34:
     print("Your grade is D")
else:
     print("Invalid Input")
     

