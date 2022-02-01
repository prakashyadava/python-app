row1 = ["11", "21", "31"]
row2 = ["12", "22", "32"]
row3 = ["13", "23", "33"]
print(f"{row1}\n{row2}\n{row3}")
map = [row1, row2, row3]
pos = input("Where do you want to put the treasure: ")
hor = int(pos[1]) -1
ver = int(pos[0]) -1
map[hor][ver] = "X"

print(f"{row1}\n {row2} \n {row3}")
