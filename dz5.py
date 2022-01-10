import tkinter as tk
import random
import time

colors = ["red", "yellow", "blue", "green"]
random_color = 3
start_time = 0
end_time = 0
rclick = 0
wclick = 0

window = tk.Tk()


window.geometry("300x300")
label = tk.Label(
    text="Timer Calculator",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=100,
    height=2
)
label_right = tk.Label(
    text="Правильные: 0",
    foreground="green"

)

label_wrong = tk.Label(
    text="Неправильные: 0",
    foreground="red"

)

def send_message():
    global end_time
    global rclick,wclick
    if random_color == 0:
        end_time = time.time()
        difference = round(end_time - start_time,3)
        result.config(text=f"Реакция: {difference} сек.")
        rclick = rclick+1
        label_right.config(text=f"Правильные: {rclick}")
    else:
        list_msg = ["И снова нет)","Ты что дальтоник?","Уже выпил?","Ручки дрожат?"]
        result.config(text= list_msg[random.randint(0,3)])
        wclick = wclick+1
        label_wrong.config(text=f"Неправильные: {wclick}")
button = tk.Button(
    text="Click me if red",
    bg="blue",
    fg="yellow",
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


label_wrong.pack(anchor = "e", side = "bottom")
label_right.pack(anchor = "w", side = "bottom")

def timer_update():
    global random_color
    global start_time
    random_color = random.randint(0,3)
    label.config(background=colors[random_color])
    if random_color == 0:
        start_time = time.time()

    window.after(random.randint(500,2500), timer_update)
window.after(random.randint(500,2500), timer_update)



window.mainloop()
