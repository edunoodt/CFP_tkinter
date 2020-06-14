from tkinter import *

def valor_cuota ():
    total = float(monto_Entry.get())
    cuotas = float(cuotas_Entry.get())
    int_dic={'0-2':0,'3-6':0.1,'7-12':0.2,'13-18':0.3}
    if cuotas < 19:
        if cuotas < 3:
            int=int_dic['0-2']
        elif 3<=cuotas<7:
            int=int_dic['3-6']
        elif cuotas<13:
            int=int_dic['7-12']
        else:
            int=int_dic['13-18']

        cuota = round((total / (1 - (1 + int) ** (-cuotas))) * int / (1 + int),2)
        ValorCuota_Lbl.configure(text='$' + str(cuota), relief='sunken', bg='white', font=('arial', 12))
    else:
        ValorCuota_Lbl.configure(text='18 cuotas màximo', relief='sunken', bg='white', font=('arial', 12))

main = Tk()

main.title('Calculadora de Financiación')
#main.geometry ('400x200')

monto_Lbl=Label(text='Pago Total')
monto_Lbl.grid(row=0,column=0)
monto_Entry = Entry(main)
monto_Entry.grid(row=0,column=1, padx=20, pady=20)

cuotas_Lbl=Label(text='Cantidad de cuotas')
cuotas_Lbl.grid(row=1,column=0)
cuotas_Entry = Entry(main)
cuotas_Entry.grid(row=1,column=1, padx=20, pady=20)


ValorCuotaTxt_Lbl= Label(main,text='Valor de la cuota:')
ValorCuotaTxt_Lbl.grid(row=2 , column=0)
ValorCuota_Lbl = Label(main,text='Ingrese Monto total y cantidad de cuotas',relief='sunken',bg='white',font=('arial',8))
ValorCuota_Lbl.grid(row=2 , column=1, padx=20, pady=20)

"""
valorCuota_Lbl=Label(text='Valor de cada cuota')
valorCuota_Lbl.grid(row=2,column=0)
valorCuota_Entry = Entry(main)
valorCuota_Entry.grid(row=2,column=1)"""

monto_BTN = Button(text = 'calcule la Financiación', command = valor_cuota, width=50)
monto_BTN.grid(row=3, columnspan=2, pady=20)



mainloop()