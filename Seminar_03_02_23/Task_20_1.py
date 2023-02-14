# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод: ноутбук; Вывод: 12

dict_latin = [{1: "A, E, I, O, U, L, N, S, T, R"}, {2: "D, G"}, {3: "B, C, M, P"}, {4: "F, H, V, W, Y"},
            {5: "K"}, {8: "J, X"}, {10: "Q, Z"}]

word = input('Enter the word: ').upper()
length_word = len(word)
sum_values = 0

for i in range(length_word):
    for element in dict_latin:   
        for v in element:
            if word[i] in element[v]:
                sum_values += v
print(sum_values)

# for element in t:
#     for v in element:
#         if "S005" in element[v]:
# print(s)

# list_1 = ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"]
# list_2 = ['D', 'G']
# list_3 = ['B', 'C', 'M', 'P']
# list_4 = ['F', 'H', 'V', 'W', 'Y']
# list_5 = ['K']
# list_8 = ['J', 'X']
# list_10 = ['Q', 'Z']
# dict_latin = {}
# for element in list_1:
#     dict_latin[element] = 1

# for element in list_2:
#     dict_latin[element] = 2

# for element in list_3:
#     dict_latin[element] = 3

# for element in list_4:
#     dict_latin[element] = 4

# for element in list_5:
#     dict_latin[element] = 5

# for element in list_8:
#     dict_latin[element] = 8

# for element in list_10:
#     dict_latin[element] = 10
# str = input('Enter the word: ').upper()

# for i in range(str.count()):
#     if str[i] in 