print(2)
print(3)
for i in range(3, 110000, 2):
    if i < 10 or i % 10 != 5:
        for j in range(3, i, 2):
            if j * j > i:
                print(i)
                break
            if i % j == 0:
                break
