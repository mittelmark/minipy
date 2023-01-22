"""
Command-line application example for minipy package.
"""
import minipy
import sys

def run():
    print("This is the minipy adder!\nEnter two numerical values!\n")

    x=int(input("Enter first  number: "))
    y=int(input("Enter second number: "))

    z=minipy.add(x,y)

    print("\nThe result is: "+str(z)+"!")

    print("")

    print("Command line arguments where: " + ", ".join(sys.argv)+"\n")

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print("Usage: python3 -m minipy\nVersion:\t"+minipy.__version__+"\nAuthor:\t"+minipy.__author__)
    else:
        run()
