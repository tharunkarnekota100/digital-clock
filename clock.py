from tkinter import *
from time import strftime

main_window = Tk()
main_window.title('Digital clock')
main_window.geometry('630x135')  # size of window
main_window.minsize(630, 135)
main_window.maxsize(630, 135)
main_window.config(bg='red')  # we can also take black for more beautiful,it will cover only remaining part of label


def good_time():
    cur_time = strftime('%I:%M:%S %p')  # i for 12 hrs and h for 24 hrs         //%p gives am or pm
    clock_label.config(text=cur_time)
    clock_label.after(1000, good_time)  # 1000 milliseconds = 1 second , after every one second it should
    # call the function ie recurtion


clock_label = Label(main_window, text='Digital clock', font=('Arial', 80), bg='black', fg='#03fc3d', padx=5, pady=5)
clock_label.pack()

good_time()

main_window.mainloop()
