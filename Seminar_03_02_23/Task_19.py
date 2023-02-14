# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_input = [1, 2, 3, 4, 5]
list_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3

# list_result = []
# for i in range(k, len(list_input)):
#     list_result.append(list_input[i])
# for i in range(k):
#     list_result.append(list_input[i])
# print(list_result)
# print(list_input[-k + 1:]+list_input[:k])
# print(list_input[k:] + list_input[:k])
# print(list_input[-k:] + list_input[:len(list_input) - k])
print(list_input[1:])