import tkinter as tk
from math import ceil
from tkinter import messagebox

def btnCalcular():
    monto=250.0
    peso=float(peso_wdow.get())
    monto=monto+25*ceil(peso-10) if peso>10.0 else monto
    monto=0.85*monto if flg_Particular.get() else monto
    monto=1.25*monto if flg_Urgente.get() else monto
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
btn_wdow.grid(row=1 , column=1)

flg_Particular=tk.IntVar()
chk_Part_wdow = tk.Checkbutton(wdow,text = 'Cliente Particular',variable=flg_Particular)
chk_Part_wdow.grid(row=2,column=0)

flg_Urgente=tk.IntVar()
chk_Urg_wdow = tk.Checkbutton(wdow,text = 'Envío Urgente',variable=flg_Urgente)
chk_Urg_wdow.grid(row=3,column=0)


wdow.mainloop()