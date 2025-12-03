while True:
    c = input("Carácter: ")
    if c == " ": break
    if c.lower() in "aeiou":
        print("VOCAL")
    else:
        print("NO VOCAL")
