
count = 0
for i in range(100, 1000):
    if (i % 5 == 0 or i % 6 == 0) and not(i % 5 == 0 and i % 6 == 0):
        print(i, end=" ")
        count += 1
        if count % 10 == 0:
            print()