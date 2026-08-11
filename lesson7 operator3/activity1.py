x=5
if type(x) is int:
    print("true:it is int")
else:
    print("false:it is not int")

x=5.6
if type(x) is float:
    print("true:it is float")
else:
    print("false:it is not float")

x=10
y=20
if x is y:
    print("x and y have identical values")
else:
     print("x and y have not identical values")


if x is not y:
    print("x and y have not identical values")
else:
     print("x and y have identical values")
