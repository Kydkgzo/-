import io
from collections import Counter

r_file = io.open("voina.txt", mode="r", encoding="utf-8")

txt = r_file.read()

txt1 = txt.split()
counter = 0
i=0
txt2 = []
# больше двух букв
for i in range(len(txt1)):
    if len(txt1[i]) >2:
        counter +=1
    if len(txt1[i]) >3:
        txt2.append(txt1[i])
    i=i+1

print(f"Количество слов больше двух букв: {counter}")

best = 0
# самое длинное слово
for index in range(len(txt1)):
    if len(txt1[index])> len(txt1[best]):
        best = index
print(f"Самое длинное слово в тексте: {txt1[best]}")

# список самых популярных слов
freq_list = Counter(txt2)
most_popular = freq_list.most_common(3)
print(f"Чаще всего встречаются такие слова как: {most_popular}")





