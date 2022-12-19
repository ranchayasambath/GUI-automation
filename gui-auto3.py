import tkinter as tk
from tkinter import ttk
import re,np
import pyperclip


window = tk.Tk()



window.title("Python Calculator")
window.minsize(10,50)

userInput = window.clipboard_get()
# print(userInput)

# Function to isolate the number 
def clickMe():
    # Will use .txt's path from user input
    # text = open(input.get())

    text = userInput
    final = []
    for line in text:    
        # Remove spacing from the start and at the end
        print(line)
        line = line.strip()
        # Regex + re.match library to find the value 
        # It looks for a value starting after logical reads(space)
        # And ends at comma.
        match = re.findall('(?<=logical reads )[^,]*',line)

        # Skip any value that doesn't exist
        if len(match) > 0:
            # Store the sum of matched numbers for all the rows
            # Then convert the number into MB.
            # Multiply 8096 then divide the final result by 1000000
            lineVal = (sum(map(int, match))*8096)/1000000
            # Append result to the blank array previously assigned to variable "final"
            final.append(lineVal)
    label.configure(text= ("Final sum = {: ,} ".format(int(np.sum(final))) + "MB") )
    # input.set('')
label = ttk.Label(window, text = "Enter your path: ")
label.grid(column = 0, row=0)


# input = tk.StringVar()
# pathInput = ttk.Entry(window, width=50, textvariable= input)
# pathInput.grid(column=0, row=1)

button = ttk.Button(window, text = "Calculate", command = clickMe)
button.grid(column=0)

window.mainloop()
