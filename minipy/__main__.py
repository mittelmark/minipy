import minipy
import sys

print("This is the minipy adder!\nEnter two numerical values!\n")

x=int(input("Enter first  number: "))
y=int(input("Enter second number: "))

z=minipy.add(x,y)

print("\nThe result is: "+str(z)+"!")

print("")

print("Command line arguments where: " + ", ".join(sys.argv)+"\n")
