n = 10

for i in range(n):
    if i < 3:
        print(f"INFO i: {i}")
    elif i <=5:
        print(f"WARNING i: {i}") 
    elif i <= 7:
        print(f"ERROR i: {i}")
    else:
        print(f"CRITICAL i: {i}")