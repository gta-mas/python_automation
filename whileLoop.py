a = 10

while a > 1:
    if a == 9:
        a = a - 1  
        continue
    if a == 3:
        break
    print(a)
    a = a - 1

print("While loop finished")