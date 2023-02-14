# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# str_result = str_input[0] + " "
# count_temp = {str_input[0]: 1}
# list_unique = [str_input[0]]

# count_temp [str_input[1]] = 2
# print(count_temp.get(str_input[1]))
# print(count_temp)
# count_1 = count_temp[str_input[1]]
# print("%s :: %d" % (str_input[0], count_1))

# for i in range(1, len(str_input)):
#     letter_temp = str_input[i]
#     str_result = str_result + letter_temp
#     if  letter_temp in list_unique:
#         str_result = str_result + "_" + str(count_temp.get(letter_temp)) + " "
#         count_temp [letter_temp] += 1
#     else:
#         str_result = str_result + " "
#         count_temp [letter_temp] = 1       
#         list_unique.append(letter_temp)
# print(str_result)
str_input = input('Enter string: ').split(" ")
result = dict()
str_result = ""
for char in str_input:    
    if char in result:
        str_result = str_result + "%s_%d " % (char, result[char])
        # print(f"{char}_{result[char]}", end=" ")
    else:
        str_result = "".join([str_result, char]) + " "
        # print(f"{char}", end=" ")
    result[char] = result.get(char, 0) + 1
print(str_result)
