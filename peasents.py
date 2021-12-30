from tkinter import *

root = Tk()
root.title("sales application")
root.geometry("750x750")

month = Label(root)
profits = Label(root)
max_money = Label(root)
min_money = Label(root)

profitsv = (1000000, 2, 999, 1, -23, -999, 5, 9999, -9999, 10, 0.9, 99999)
monthv = "Janaury", "Fabulouslyry", "Merch", "Apprill", "Mayo", "Junne", "Jubily", "Agust", "Septempber", "Oxober", "Noviceber", "Declerationber"

month["text"] = "Janaury, Fabulouslyry, Merch, Apprill, Mayo, Junne, Jubily, Agust, Septempber, Oxober, Noviceber, Declerationber"

profits["text"] = "1000000, 2, 999, 1, -23, -999, 5, 9999, -9999, 10, 0.9, 99999"

def max_stuff():
    yum = max(profitsv)
    yum2 = max(monthv)
    max_money["text"] = "maximum money was earned was the moth of " + str(yum2) + " with $" + str(yum) + " earned"

def min_stuff():
    yum3 = min(profitsv)
    yum4 = min(monthv)
    min_money["text"] = "minimum money was earned was the moth of " + str(yum4) + " with $" + str(yum3) + " earned"

btn = Button(root, text = "max money here", command = max_stuff)
btn1 = Button(root, text = "min money here", command = min_stuff)



month.place(relx = 0.5, rely = 0.3, anchor = CENTER)
profits.place(relx = 0.5, rely = 0.4, anchor = CENTER)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
max_money.place(relx = 0.5, rely = 0.6, anchor = CENTER)
btn1.place(relx = 0.5, rely = 0.7, anchor = CENTER)
min_money.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()