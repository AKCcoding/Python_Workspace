a = input("Do you Agree: ")

#another method for efficiency so that you won't declare it twice
a = a.lower()

if a in ["yes","y"]:
    print("Agrees")
elif a in ["no","n"]:
    print("Disagrees")

