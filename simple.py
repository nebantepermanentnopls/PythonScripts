# 2 3 5 7 ..
# самый простой алг
# for i in range(1, 200000):
#    k = 0
#    for j in range(2, i-1):
#        if i % j == 0:
#            k += 1
#    if k == 0:
#        print(i)

simple = []
for i in range(2, 500):
    for j in simple:
        if i % j == 0:
            break
    else:
        simple.append(i)

print(simple)

