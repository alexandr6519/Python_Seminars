print("Введите текст")
text = input().split()
s = set()
for word in text:
    s.add(word.lower())
print(len(s))