# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
print('Введите число n:')
n = int(input())
list1 = list(map(int, input().split()))
print('Введите число m:')
m = int(input())
list2 = list(map(int, input().split()))
# for i in range(n):
#     flag = False
#     for j in range(m):
#         if list1[i] == list2[j]:
#             flag = True
#             break
#     if not flag:
#         print(list1[i], end=' ')
s1 = set(list2)
for i in range(n):
    if list1[i] not in s1:
        print(list1[i], end=' ')