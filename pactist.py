# break


while True:
    name = input("entre you name: ")
    if name != "":
        break


# continue


phone_number = "076-555-1234"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")


# pass


for i in range(1,21):
    if i ==13:
        pass
    else:
        print(i)