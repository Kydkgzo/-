name = input("введите свое имя : ")
age = int(input("укажите ващ возраст : "))
agelist = [" годик"," года"," лет"]
age1 = 0
if age == 1:
    age1 = 0
elif age in range(2,4):
    age1 = 1
else:
    age1 = 2

print("Привет " + name + ", тебе уже " + str(age) + agelist[age1] + " это здорово! ")
