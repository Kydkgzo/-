import tkinter as tk
import random
import time

colors = ["red", "yellow", "blue", "green"]
# убраны переменные которые избыточны (но это не обязательно)
start_time = 0
rclick = 0
wclick = 0

window = tk.Tk()

window.geometry("300x300")
bottom_frame = tk.Frame(window)
bottom_frame.pack(side="bottom")

label = tk.Label(
        text="Timer Calculator",
        foreground="white",  # Set the text color to white
        background="black",  # Set the background color to black
        width=100,
        height=2
)
label_right = tk.Label(bottom_frame,
                       text="Правильные: 0",
                       foreground="green"

                       )

label_wrong = tk.Label(bottom_frame,
                       text="Неправильные: 0",
                       foreground="red"

                       )


def send_message():
    global rclick, wclick
    if label["background"] == "red":
        difference = round(time.time() - start_time, 3)
        result.config(text=f"Реакция: {difference} сек.")
        rclick = rclick + 1
        label_right.config(text=f"Правильные: {rclick}")
        label.config(background="grey") # добавленно чтоб сменить цвет и небыло повторного нажатия
    else:
        list_msg = ["И снова нет)", "Ты что дальтоник?", "Уже выпил?",
                    "Ручки дрожат?"]
        result.config(text=list_msg[random.randint(0, 3)])
        wclick = wclick + 1
        label_wrong.config(text=f"Неправильные: {wclick}")
        label.config(background="grey")
        window.update() # обновляет изображение можно убрать и посмотреть в чем разница 
        time.sleep(1) # добавляет секнду к фолс нажатию, чтоб не возможно было использовать сильно частые клики


button = tk.Button(
        text="Click me if red",
        background="blue",
        width=12,
        height=1,
        command=send_message
)

result = tk.Label(
        text="0.0",
        foreground="red",  # Set the text color to white
        font=("Arial", 25)
)

for c in window.children:
    window.children[c].pack()

label_wrong.pack(side="left")
label_right.pack(side="right")


def timer_update():
    global start_time
    label.config(background=colors[random.randint(0, 3)])
    if label["background"] == "red":
        start_time = time.time()

    window.after(random.randint(500, 2500), timer_update)


window.after(random.randint(500, 2500), timer_update)

window.mainloop()
