import tkinter, customtkinter,re ,np

customtkinter.set_appearance_mode("System") # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue") # Themes: blue (default), dark-blue, green

app = customtkinter.CTk() # create CTk window like you do with the Tk window

app.geometry("400x240")
app.title("Calculator")

def button_function():
    # print("button pressed")
    usrInput = input("Stop asking me to calculate, Enter dir path: ")
# text = open('C:/Users/ranch/Downloads/jack.txt')
    text = open(usrInput)
    final = []
    for line in text:
        line = line.strip()
        match = re.findall('(?<=logical reads )[^,]*',line)

        if len(match) > 0:
            lineVal = (sum(map(int, match))*8096)*1000000
            final.append(lineVal)
            #  print("line sum = {0}".format(lineVal))
    write = open('result.txt' , 'w')
    write.write("Final sum = {: ,} ".format(np.sum(final)) + "MB") 

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Calculate", command=button_function)
button.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)

app.mainloop()