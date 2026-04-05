#pythagoreous theorem
import math
x=float(input("Enter the length of side A (in cm):"))
y=float(input("Enter the length of side B (in cm):"))
z= math.sqrt(pow(x,2)+pow(y,2))
print(f"The length of side C is {round(z,2)} cm")
