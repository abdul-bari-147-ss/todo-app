try:
    width = float(input("enetr rectangle width:"))
    length = float(input("enter rectangle length:"))
    if width==length:
       print("that looks like a square.")
       exit()

    print("Area is ",width * length )
except ValueError:
    print("Please enter a number.")