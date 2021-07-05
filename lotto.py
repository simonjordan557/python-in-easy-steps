# Widgets:

from tkinter import *

window = Tk()

title_label = Label(window, text = 'GOOD LUCK!')
label_1 = Label(window, relief = 'groove', width = 2)
label_2 = Label(window, relief = 'groove', width = 2)
label_3 = Label(window, relief = 'groove', width = 2)
label_4 = Label(window, relief = 'groove', width = 2)
label_4 = Label(window, relief = 'groove', width = 2)
label_5 = Label(window, relief = 'groove', width = 2)
label_6 = Label(window, relief = 'groove', width = 2)
getBtn = Button(window)
resBtn = Button(window)

# Geometry:

title_label.grid(row = 1, column = 1, rowspan = 2, pady = 10)
label_1.grid(row = 1, column = 2, padx = 10, pady = 10)
label_2.grid(row = 1, column = 3, padx = 10, pady = 10)
label_3.grid(row = 1, column = 4, padx = 10, pady = 10)
label_4.grid(row = 1, column = 5, padx = 10, pady = 10)
label_5.grid(row = 1, column = 6, padx = 10, pady = 10)
label_6.grid(row = 1, column = 7, padx = (10, 20), pady = 10)
getBtn.grid(row = 2, column = 2, columnspan = 4, pady = 10)
resBtn.grid(row = 2, column = 6, columnspan = 2, pady = 10)

# Static Properties:

window.title('Lotto Number Picker')
window.resizable(0, 0)
getBtn.configure(text = 'Get My Lucky Numbers')
resBtn.configure(text = 'Reset')

# Initial Properties:

label_1.configure(text = '...')
label_2.configure(text = '...')
label_3.configure(text = '...')
label_4.configure(text = '...')
label_5.configure(text = '...')
label_6.configure(text = '...')
resBtn.configure(state = DISABLED)

# Dynamic Properties:

from random import sample

def pick():
	nums = sample(range(1, 60), 6)
	nums.sort()
	label_1.configure(text = nums[0])
	label_2.configure(text = nums[1])
	label_3.configure(text = nums[2])
	label_4.configure(text = nums[3])
	label_5.configure(text = nums[4])
	label_6.configure(text = nums[5])
	getBtn.configure(state = DISABLED)
	resBtn.configure(state = NORMAL)

def reset():
	label_1.configure(text = '...')
	label_2.configure(text = '...')
	label_3.configure(text = '...')
	label_4.configure(text = '...')
	label_5.configure(text = '...')
	label_6.configure(text = '...')
	getBtn.configure(state = NORMAL)
	resBtn.configure(state = DISABLED)

# Functionality:

getBtn.configure(command = pick)
resBtn.configure(command = reset)

# Sustain Window:

window.mainloop()




