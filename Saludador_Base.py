import tkinter as tk
from tkinter import messagebox


def btnSaludar():
    texto='¡¡¡Hola '+txtNombre.get()
    if flagSonrisa.get() == 1:
        texto = texto + ' :) '
    texto = texto + '!!!'
    messagebox.showinfo('Saludo',texto)


root = tk.Tk()
root.title('Saludador')
root.geometry('400x150')


btnSaludar = tk.Button(root,text='Saludar',fg='white',bg='blue',command=btnSaludar)
btnSaludar.grid(row=2,column=0)
lblTexto = tk.Label(root,text='¿A quien saludamos?',font=('Arial',30))
lblTexto.grid(row=0,column=0,columnspan=2)
txtNombre = tk.Entry(root)
txtNombre.grid(row=1,column=0)
flagSonrisa=tk.IntVar()
chkSonrisa = tk.Checkbutton(root,text = 'Agregar :)', variable=flagSonrisa)
chkSonrisa.grid(row=1,column=1)

root.mainloop()


