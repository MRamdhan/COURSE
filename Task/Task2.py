N = int(input(" Ukuran Grid : "))
commends = input()
x,y = 1,1

for commend in commends:
    if commend == "U" and x < N:
        x += 1
    elif commend == "D" and x > 1:
        x -= 1
    elif commend == "L" and y > 1:
        y -= 1
    elif commend == "R" and y < N:
        y += 1

print(x,y)