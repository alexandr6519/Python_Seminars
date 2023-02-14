# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list_input = [1, 1, 2, 0, 1, 5, 2, -1, 3, 4, 4]

# count = 0
# list_unique = []
# for element in list_input:
#     if element not in list_unique:
#         list_unique.append(element)
# print(len(list_unique))

# print(len(set(list_input)))
k = 8
print(list_input[k:] + list_input[:k])
