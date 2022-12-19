import tkinter as tk
from tkinter import ttk
import re,np
import pyperclip


window = tk.Tk()

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
print(finalSum)