from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Listbox Example')

frame = Frame(window)
listbox = Listbox(frame)
listbox.insert(1, 'HTML In Easy Steps')
listbox.insert(2, 'CSS In Easy Steps')
listbox.insert(3, 'Javascript In Easy Steps')

def dialog():
	box.showinfo('Selection', 'Your Choice: ' + listbox.get(listbox.curselection()))

btn = Button(frame, text = 'Choose', command = dialog)

btn.pack(side = RIGHT, padx = 5)
listbox.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)

window.mainloop()
