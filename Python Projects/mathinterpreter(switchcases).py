user = input("enter arithmetic expression").strip( )

x,y,z=user.split()
x=float(x)
z=float(z)

match y:
    case "+":
        print(x+z)
    case "/":
        print(x/z)
    case "-":
        print(x-z)
    case "*":
        print(x*z)
    case "_":
        print("Invalid")


