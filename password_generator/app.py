#Importar librerías
from tkinter import *
import string
import random
from random import randint
import pyperclip

#Crear Ventanas
root = Tk()
colorBg= "#2A2F4F"
root.config(bg= colorBg)
root.title("Password Generator")
root.iconbitmap('password.ico')
root.geometry("450x550")

choice = IntVar()
Font= ("Courier", 16)

#Funciones
def generate():
    small_alphabets = string.ascii_lowercase
    capital_alphabets= string.ascii_uppercase
    numbers= string.digits
    special_characters= string.punctuation

    all= small_alphabets + capital_alphabets + special_characters
    #print(all) Verificar
    password_length= int(length_box.get()) #Entero

    e1.delete(0,END)

    if choice.get()== 1:
        e1.insert(0, random.sample(small_alphabets,password_length))
    if choice.get()== 2:
        e1.insert(0, random.sample(small_alphabets+capital_alphabets,password_length))
    if choice.get()== 3:
        e1.insert(0, random.sample(all,password_length))

    #password= random.sample(all, password_length) #Generar contraseña
    #e1.insert(0, password) #Insertar

def copy():
    random_password= e1.get()
    pyperclip.copy(random_password)
    e1.delete(0,END)

def delete():
    e1.delete(0,END)


# Interfaz

label1= Label(root, text= "Password Generator", font= ("Courier", 28), bg= colorBg, fg="white", anchor= CENTER , justify= CENTER)
label1.grid(padx= 10)

labelframe1 = LabelFrame(bg=colorBg, text="Type", fg= "white", font="Courier")
labelframe1.grid()

weakradiobtn = Radiobutton(labelframe1, text= "Weak", value= 1, variable = choice, font=Font, fg= "white", bg= colorBg)
weakradiobtn.grid(pady= 5, padx= 10)

mediumradiobtn = Radiobutton(labelframe1, text= "Medium", value= 2, variable= choice, font= Font, fg= "white", bg= colorBg)
mediumradiobtn.grid(pady= 5, padx= 10)

strongradiobtn = Radiobutton(labelframe1, text= "Strong", value= 3, variable= choice, font= Font, fg= "white", bg= colorBg, highlightcolor=  "black", highlightbackground="yellow")
strongradiobtn.grid( pady= 5, padx= 10)

labelframe2 = LabelFrame(bg= colorBg, text="Password Lenght", fg= "white", font="Courier")
labelframe2.grid(pady= 15)

length_box = Spinbox(labelframe2, from_= 5, to_= 10, width= 4, font= Font, wrap= True)
length_box.grid(padx= 10, sticky= "e", pady= 10)

generateBtn = Button(root, text= "Generate", font= Font, command= generate )
generateBtn.grid(pady= 20)

e1 = Entry(root, width=25, bd=2, font=Font)
e1.grid()

labelframe2 = LabelFrame(root, text= "Buttons", fg="white", font="Courier", bg= colorBg)
labelframe2.grid(pady= 20, padx= 20, ipadx= 5 )

copyBtn = Button(labelframe2, text= "Copy", font= Font, command= copy , width= 8)
copyBtn.grid(row= 0, column= 0, pady= 10)

copyBtn = Button(labelframe2, text= "Delete", font= Font, command= delete,  width= 8 )
copyBtn.grid(pady= 10, row=0 , column= 1)

root.mainloop()