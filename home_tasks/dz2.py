name = input("введите свое имя : ")
age = int(input("укажите ващ возраст : "))
agelist = [" год"," года"," лет"]
age1 = 0
age_split = int(round((age/10 % 1),1) * 10) # возраст делим на 10, потом берем десятичную часть, округляем ее до одного знака после запятой, умножаем на 10 и приобразуем из float в int
if age != 11 and age_split == 1:
    age1 = 0
elif age != 11 and age_split in range(2,4):
    age1 = 1
else:
    age1 = 2
print("Привет " + name + ", тебе уже " + str(age) + agelist[age1] + " это здорово! ")
