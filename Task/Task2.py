N = int(input(" Ukuran Grid : "))
commends = input()
x,y = 1,1

for command in commends:
    if command == "U" and x < N:
        x += 1
    elif command == "D" and x > 1:
        x -= 1
    elif command == "L" and y > 1:
        y -= 1
    elif command == "R" and y < N:
        y += 1

print(x,y)