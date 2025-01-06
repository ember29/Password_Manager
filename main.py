from tkinter import *
from tkinter import messagebox, Entry
from random import choice,randint,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project




def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols=[choice(symbols) for s in range(randint(2, 4))]
    password_numbers=[choice(numbers) for n in range(randint(2, 4))]

    password_list=password_letters+password_symbols+password_numbers

    shuffle(password_list)

    password="".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    input_of_pass.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=input_of_website.get()
    email=input_of_email.get()
    password=input_of_pass.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website)==0 or len(password)==0:
        empty_popup=messagebox.showerror(title="Oops",message="PLease do not field empty..!! ")
    else:
            try:
                with open("data.json","r") as datafile:
                    data=json.load(datafile)
            except FileNotFoundError:
                with open("data.json","w") as datafile:
                    json.dump(data,datafile,indent=4)
            else:
                data.update(new_data)
                with open("data.json","w") as datafile:
                    json.dump(data,datafile ,indent=4)
            finally:
                input_of_website.delete(0,END)
                input_of_pass.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=30,pady=30)


canvas=Canvas(width=200,height=200)
pass_manager_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_manager_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

email_or_username_label=Label(text="Email/Username:")
email_or_username_label.grid(row=2,column=0)

pass_label=Label(text="Password:")
pass_label.grid(row=3,column=0)

input_of_website=Entry(width=39)
input_of_website.grid(row=1,column=1,columnspan=2)
input_of_website.focus()

input_of_email=Entry(width=39)
input_of_email.grid(row=2,column=1,columnspan=2)
input_of_email.insert(0,"vinayak@gmail.com")

input_of_pass=Entry(width=21)
input_of_pass.grid(row=3,column=1)

generate_pass_button=Button(text="Generate Password",command=pass_generator)
generate_pass_button.grid(row=3,column=2)

add_button=Button(text="Add",width=33,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()