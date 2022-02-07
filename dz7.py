import random
from tkinter import *
from tkinter import messagebox
import time
from datetime import datetime
import csv
from os.path import exists
database_filename = "results.csv"
window = Tk()
current_username = ""
username = StringVar()
current_color = StringVar()
window.geometry("400x400")
window.title("Проверка реакции")
start_frame = Frame(window)
start_frame.pack()
def get_username():
    global current_username
    current_username = username.get()
    if current_username.isalpha() and len(current_username) >= 2:
        start_frame.destroy()
        main_frame.pack()
    else:
        username_error.pack(side="bottom")

def timer():
    global rclick, wclick,react_avg, time_spend
    if header_button["background"] == "red":
        difference = round(time.time() - start_time, 3)
        result.config(text=f"Реакция: {difference} сек.")
        rclick = rclick +1
        time_spend = time_spend + difference
        react_avg = time_spend/rclick
        header_button.config(bg="blue")
    else:
        list_msg = ["И снова нет)", "Ты что дальтоник?", "Уже выпил?",
                    "Ручки дрожат?"]
        result.config(text=list_msg[random.randint(0,3)])
        wclick = wclick +1
    label_wrong.config(text=f"Неправильные: {round(wclick/ (rclick + wclick) * 100,1)}%")
    label_right.config(text=f"Правильные: {round(rclick / (rclick + wclick) * 100,1)}%")

    window.update()  # обновляет изображение можно убрать и посмотреть в чем разница
    time.sleep(1)  # добавляет секнду к фолс нажатию, чтоб не возможно было использовать сильно частые клики

def plus_user():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    tmp_to_write = []
    tmp_item = {}
    right_answer_percent = round(rclick/ (rclick + wclick) * 100,1)
    if right_answer_percent > 50:
        if not exists(database_filename):
            with open(database_filename,"w+") as nf:
                nf.write("username;right_answer;avg;date\r")
        with open(database_filename, encoding='utf-8') as r_file:
            file_reader = csv.DictReader(r_file, delimiter=";")
            rows = list(file_reader)
        check = [i for i in rows if i['username'] == current_username]
        if len(check) >= 1:
            for index,item in enumerate(rows):
                if item["username"] == current_username:
                    tmp_item = item
                    tmp_item["right_answer"] = right_answer_percent
                    tmp_item["avg"] = react_avg
                    tmp_item["date"] = dt_string
                    tmp_to_write.append(tmp_item)
                else:
                    tmp_to_write.append(item)
            with open(database_filename, mode="w+", encoding='utf-8') as w_file:
                file_writer = csv.DictWriter(w_file, delimiter=";", lineterminator="\r",fieldnames=("username", "right_answer", "avg","date"))
                file_writer.writeheader()
                file_writer.writerows(tmp_to_write)
        else:
            tmp_item = {"username": current_username, "right_answer":right_answer_percent, "avg":react_avg,"date":dt_string}
            with open(database_filename, mode="a", encoding='utf-8') as w_file:
                file_writer = csv.DictWriter(w_file, delimiter=";", lineterminator="\r",fieldnames=("username", "right_answer", "avg","date"))
                file_writer.writerow(tmp_item)
    else:
        messagebox.showwarning("Не сохранено", "У Вас слишком низкий процент правильных нажатий!")

react_avg = 0
time_spend = 0
colors = ("red","green","orange","yellow","blue","pink","purple")
start_time= 0
rclick = 0
wclick = 0
username_label= Label(start_frame,text="Введите имя пользователя",background="black",foreground="white",width="100", height="3").pack(side="top")
username_entry = Entry(start_frame,textvariable=username,bg="pink").pack(side="top",pady="15")
username_button= Button(start_frame, text="Start",command=get_username).pack(side="top")
username_error = Label(start_frame,text="Имя пользователя должно содержать\nтолько буквы и не менее двух символов",fg="red")
main_frame = Frame(window)
header_label = Label(main_frame, text = "Timer calculator", bg = "black", fg = "white", width="100", height="3").pack(side = "top")
header_button = Button(main_frame, text = "Click me if red", bg = "white",command = timer, width="25",height="3")
header_button.pack(side = "top",pady="15")
result = Label(main_frame,text="")
result.pack(side="top")
label_right = Label(main_frame,text="Правильные: 0",foreground="green")
label_wrong = Label(main_frame,text="Неправильные: 0",foreground="red")
label_wrong.pack(side="left")
label_right.pack(side="right")
button_save = Button(main_frame,text = "Сохранить", command=plus_user)
button_save.pack(side="bottom")

def timer_update():
    global start_time
    header_button.config(bg=colors[random.randint(0,len(colors)-1)])
    if header_button["background"] == "red":
        start_time = time.time()
    window.after(random.randint(500, 1500), timer_update)
window.after(random.randint(300, 1500), timer_update)



window.mainloop()
