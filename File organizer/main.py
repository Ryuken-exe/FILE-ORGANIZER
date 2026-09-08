with open("exp.txt","w") as file:
    file.write("PANEER = 70")
    file.write("\nTOFU = 52*2(104)")
    file.write("\nDahi = 50")

with open("exp.txt","r") as file:
    data = file.read()

print(data)