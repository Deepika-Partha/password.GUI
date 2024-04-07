from tkinter import *
import tkinter as tk

# Generate a window for the functions
passwords = tk.Tk()
passwords.geometry('400x400')
passwords.title('Create Password')

# Text for Directions
lab=Label(passwords, text='Please Enter a Valid Password',
          font='skia 20')
lab.pack(pady=50)

lab1=Label(passwords, text='- Minimum of 8 characters',
          font='skia 15')
lab1.pack()

lab2=Label(passwords, text='- Must have at least one number',
          font='skia 15')
lab2.pack()

lab3=Label(passwords, text='- Must have at least one special character',
          font='skia 15')
lab3.pack()

# Submits the entry
def submit():
    password = entry.get() 

    # global Labels can be accessed in reset()
    global fail_len
    global fail_num
    global fail_chars
    reset.config(state=NORMAL) # Allow user to reset screen
    
    # Does the password meet character requirements?
    if check_len(password) == False:
        fail_len = Label(text='Not enough characters, please try again')
        fail_len.config(font=('Ariel', 15))
        fail_len.config(fg='Red')
        fail_len.pack()
        submit.config(state=DISABLED)
    else:
        fail_len = Label(text='')
    # Does the password have a number?
    if check_num(password) == False:
        fail_num = Label(text='Missing a number, please try again')
        fail_num.config(font=('Ariel', 15))
        fail_num.config(fg='Red')
        fail_num.pack()
        submit.config(state=DISABLED)
    else:
        fail_num = Label(text='')
    # Does the password have a special character?
    if check_chars(password) == False:
        fail_chars = Label(text='Missing a special character, please try again')
        fail_chars.config(font=('Ariel', 15))
        fail_chars.config(fg='Red')
        fail_chars.pack()
        submit.config(state=DISABLED)
    else:
        fail_chars = Label(text='')

    if(check_chars(password) == True) & (check_num(password) == True) & (check_len(password) == True):
        counter = Label(text='Success! Your password is saved')
        counter.config(font=('Ariel', 15))
        counter.config(fg='Red')
        counter.pack()
        submit.config(state=DISABLED) # Turns button off
        reset.config(state=DISABLED)
        entry.config(state=DISABLED)
        close = Button(passwords, text='Close Out', command=closeOut)
        close.place(x=132,y=340) 

def reset():
    entry.delete(0, END) 
    fail_len.pack_forget()
    fail_num.pack_forget()
    fail_chars.pack_forget()
    submit.config(state=NORMAL)
          
# Hide and show password
count = 1
def password():
    global count
    count = count+1
    if(count%2 == 0):
        entry.config(show='')
        password.config(text='Hide Password')
    else:
        entry.config(show='*')
        password.config(text='Show Password')
              
# Close out of the window if a successful password is made
def closeOut():
    passwords.destroy()

# CHECK IF ENTRY LENGTH MEETS REQUIREMENTS
def check_len(entry):
    if (len(entry)<8):
        return False
    else:
        return True
              
#CHECK IF THE ENTRY MEETS THE NUMBER REQUIREMENTS
def check_num(entry):
    numbers = '1234567890'
    for char in entry:
        if char in numbers:
            return True
    return False
#CHECK IF THE ENTRY MEETS CHARACTER REQUIREMENTS
def check_chars(entry):
    special_characters = '!@#$%^&*-_+=|;:,.<>?~'
    for char in entry:
        if char in special_characters:
            return True  
    return False    

# MAIN 3 BUTTONS
submit = Button(passwords, text='Submit', command=submit)
submit.place(x=55,y=305)

reset = Button(passwords, text='Reset', command=reset)
reset.place(x=132,y=305)

password = Button(passwords, text='Show Password', command=password)
password.place(x=200,y=305)

# Create the user entry space
global entry
entry = Entry()
entry.config(font=('Ariel', 20))
entry.config(bg='White')
entry.config(fg='Black')
entry.insert(0,'')
entry.config(width=15)
entry.place(x=90,y=270)
entry.config(show='*')
reset.config(state=DISABLED) # Nothing to reset, will cause issue if clicked


# Execute window
passwords.mainloop()
