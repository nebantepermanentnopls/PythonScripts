# 2 3 5 7 ..
# самый простой алг
# for i in range(1, 200000):
#    k = 0
#    for j in range(2, i-1):
#        if i % j == 0:
#            k += 1
#    if k == 0:
#        print(i)


# simple = []
# for i in range(2, 500):
#    for j in simple:
#        if i % j == 0:
#            break
#   else:
#        simple.append(i)
# print(simple)

print(2)
cache = [2]      # 1000
for i in range(3, 110000, 2):
    flag = True
    if len(cache) == 1000:          # когда кэш заполнен начинаем проверку с чисел, которые лежат до 0го элемента кэша
        for j in range(2, cache[0]):
            if i % j == 0:
                flag = False
                break
    if flag:
        for j in cache:             # проверка на числа в кэшэ
            if j * j > i:           # проверка на корень
                print(i)
                cache.append(i)
                if len(cache) > 1000:   # поддерживаем постоянный размер кэша
                    del cache[0]
                break
            if i % j == 0:
                break



