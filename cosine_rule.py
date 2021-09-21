import math

#Finding a side

num1 = float(input("First: "))
num2 = float(input('Second: '))
angle = float(input('Angle: '))

print(math.sqrt(num1**2 + num2**2 - (2*num1*num2*math.cos(math.radians(angle)))))

#Finding an angle

num1 = float(input("First: "))
num2 = float(input('Second: '))
num3 = float(input('Third: '))

print(math.degrees(math.acos((num1**2 + num2**2 - num3**2)/(2*num1*num2))))