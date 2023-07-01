people = {
    "Rae" : "0991123456",
    "Kian": "0912345678"
}

name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")
else:
    print("Not Found")
