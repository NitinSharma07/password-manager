from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '#', '$', '%', '^', '&', '*', '(', ')']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    input3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_web = input1.get()
    new_id = input2.get()
    new_pass = input3.get()
    new_data = {
        new_web: {
            'email': new_id,
            'password': new_pass
        }
    }
    if new_web == "" or new_pass == "" or new_id == "":
        messagebox.askretrycancel(title='Retry', message='Field is empty!')
    else:
        try:
            with open('data.json', mode='r') as file2:
                data = json.load(file2)
        except FileNotFoundError:
            with open('data.json', mode='w') as file2:
                json.dump(new_data, file2, indent=4)
        else:
            data.update(new_data)
            with open('data.json', mode='w') as file2:
                json.dump(data, file2, indent=4)
        finally:
            input1.delete(0, END)
            input3.delete(0, END)


def find_password():
    website = input1.get()
    try:
        with open('data.json') as file2:
            data = json.load(file2)
    except FileNotFoundError:
        messagebox.showinfo(title='error', message='No data file found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(title='Error', message='No detail for website exists.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30)
new_image = PhotoImage(file='logo.png')
canvas = Canvas(width=250, height=200)
canvas.create_image(100, 100, image=new_image)
canvas.grid(row=0, column=1)

label = Label(text="website: ")
label.grid(row=1, column=0)

label2 = Label(text='Email/Username: ')
label2.grid(row=2, column=0)

label3 = Label(text='Password:')
label3.grid(row=3, column=0)

input1 = Entry(width=35)
input1.grid(row=1, column=1, columnspan=2)

input2 = Entry(width=35)
input2.grid(row=2, column=1, columnspan=2)
input2.insert(0, 'nitinsharma01002@gmail.com')

input3 = Entry(width=34)
input3.grid(row=3, column=1, columnspan=2)

button = Button(text='Generate Password', command=generate_password)
button.grid(row=3, column=2)

button2 = Button(text='Add', width=36, command=save)
button2.grid(row=4, column=1, columnspan=2)

button3 = Button(text='search', command=find_password)
button3.grid(row=1, column=2)
window.mainloop()


