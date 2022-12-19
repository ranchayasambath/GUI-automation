import tkinter as tk
from tkinter import ttk
import re,np
window =tk.Tk()

window.title("Python Calculator")
window.minsize(20,50)

def clickMe():
    final=[]
    userInput = window.clipboard_get()
    userInput = userInput.strip()
    match = re.findall('(?<=logical reads )[^,]*',userInput)
    for i in match:
        final.append(int(i))
    # print(final)
    total = 0
    for ele in range(0, len(final)):
        total = total + final[ele]
    sum = (total*8096)/1000000
    finalSum = int(round(sum))
    # print(finalSum)
    label.configure(text= "Your Total Sum is :  " +  str(finalSum) +  "  MB")
label = ttk.Label(window, text = "Ctrl + C your data: ")
label.grid(column = 0, row=0)

button = ttk.Button(window, text = "Calculate", command = clickMe)
button.grid(ipadx=100, ipady=30)

window.mainloop()
