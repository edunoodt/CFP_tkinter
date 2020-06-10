import tkinter as tk
from math import ceil
from tkinter import messagebox

def btnCalcular():
    monto=250.0
    peso=float(peso_wdow.get())
    monto=monto+25*ceil(peso-10) if peso>10.0 else monto
    msg='Envío paquete '+str(peso)+' Kg  $'+str(monto)
    messagebox.showinfo('Valor del envío',msg)



wdow=tk.Tk()
wdow.title('Servicio de Paquetería')
wdow.geometry('400x150')

lbl_wdow = tk.Label(wdow,text='Peso (Kg)',font=('Arial',30))
lbl_wdow.grid(row=0 , column=0)

peso_wdow = tk.Entry(wdow)
peso_wdow.grid(row=0 , column=1)

btn_wdow = tk.Button(wdow,text='Calcular Importe',fg='red',bg='white',command=btnCalcular)
btn_wdow.grid(row=1 , column=0, sticky='W')



wdow.mainloop()