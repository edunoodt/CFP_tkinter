import tkinter as tk

def btnCalcular():
    monto = 500*float(dias_wdow.get())+45*float(km_wdow.get())
    lbl_Valor_wdow.configure(text='$'+str(monto))


wdow = tk.Tk()
wdow.geometry('700x400')
wdow.title('Facturador de viajes')

lbl_dias_wdow = tk.Label(wdow,text='Días que utilizó el vehículo  ',font=('Arial',15))
lbl_dias_wdow.grid(row=0 , column=0)
dias_wdow = tk.Entry(wdow)
dias_wdow.grid(row=0 , column=1)

lbl_km_wdow = tk.Label(wdow,text='Km recorridos con el vehículo  ',font=('Arial',15))
lbl_km_wdow.grid(row=1 , column=0)
km_wdow = tk.Entry(wdow)
km_wdow.grid(row=1 , column=1)

lbl_Importe_wdow = tk.Label(wdow,text='Importe a Abonar  ',font=('Arial',15))
lbl_Importe_wdow.grid(row=2 , column=0)
lbl_Valor_wdow = tk.Label(wdow,text='Ingrese los días y Km utilizados  ',font=('Arial',15))
lbl_Valor_wdow.grid(row=2 , column=1)


btn_Importe= tk.Button(wdow,text='Calcular Importe',fg='red',bg='white',command=btnCalcular)
btn_Importe.grid(row=3 , column=1)



wdow.mainloop()