import tkinter as tk
from tkinter import ttk
import re,np
window =tk.Tk()

window.title("Python Calculator")
window.minsize(10,50)

def clickMe():
    text = open(input.get())
    final = []
    for line in text:
        line = line.strip()
        match = re.findall('(?<=logical reads )[^,]*',line)

        if len(match) > 0:
            lineVal = (sum(map(int, match))*8096)/1000000
            final.append(lineVal)
    label.configure(text= ("Final sum = {: ,} ".format(int(np.sum(final))) + "MB") )

label = ttk.Label(window, text = "Enter your path: ")
label.grid(column = 0, row=0)

input = tk.StringVar()
pathInput = ttk.Entry(window, width=50, textvariable= input)
pathInput.grid(column=0, row=1)

button = ttk.Button(window, text = "Calculate", command = clickMe)
button.grid(column=0)

window.mainloop()
