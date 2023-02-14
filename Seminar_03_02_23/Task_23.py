# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
numbers = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        count += 1
print(count)

# n = int(input("Enter number "))
# l = [0] * n
# print(l)
# for i in range(n):
#     l[i] = i
#     print(l[i])